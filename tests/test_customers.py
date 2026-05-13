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