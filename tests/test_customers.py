from models.create_customer_model import CustomerResponse


def test_create_customer(stripe_api):

    data = {
        'email': 'John@gmail.com',
        'name': 'Doe',
    }

    response = stripe_api.post(f'customers', data=data)

    assert response.status_code == 200, f'Expected 200, got response {response.status_code}'


    customer = CustomerResponse(**response.json())
    assert customer.email == data['email']
    assert customer.name == data['name']

    del_response = stripe_api.delete_customer(customer.id)
    assert del_response.status_code == 200


def test_create_new_customer_with_valid_data(customer_payload_factory, stripe_api):
    payload  = customer_payload_factory()

    responses = stripe_api.post(f'customers', data=payload)
    assert responses.status_code == 200, f'Expected 200, got response {responses.status_code}'

    body = responses.json()
    assert body['email'] == payload['email']
    assert body['name'] == payload['name']


def test_created_customer_fixture_returns_customer(created_customer):
    assert created_customer["id"] is not None
    assert created_customer["object"] == "customer"
    assert "@" in created_customer["email"]



def test_retrieve_created_customer(created_customer, stripe_api):
    customer_id = created_customer["id"]

    response = stripe_api.get(f"customers/{customer_id}")

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == customer_id
    assert body["object"] == "customer"
    assert body["email"] == created_customer["email"]
    assert body["name"] == created_customer["name"]


def test_update_created_customer_name(created_customer, stripe_api):
    customer_id = created_customer["id"]

    update_payload = {
        "name": "Updated Test Customer"
    }

    response = stripe_api.post(f"customers/{customer_id}", data=update_payload)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == customer_id
    assert body["object"] == "customer"
    assert body["name"] == "Updated Test Customer"
    assert body["email"] == created_customer["email"]


def test_delete_created_customer(stripe_api, customer_payload_factory):
    payload = customer_payload_factory()

    create_response = stripe_api.post("customers", data=payload)
    assert create_response.status_code == 200

    customer = create_response.json()
    customer_id = customer["id"]

    delete_response = stripe_api.delete(f"customers/{customer_id}")
    assert delete_response.status_code == 200

    body = delete_response.json()

    assert body["id"] == customer_id
    assert body["object"] == "customer"
    assert body["deleted"] is True