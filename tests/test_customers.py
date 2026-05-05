from models.create_customer_model import CustomerResponse


def test_create_customer(stripe_api):

    data = {
        'email': 'John@gmail.com',
        'name': 'Doe',
    }

    response = stripe_api.post(f'customers', data=data)
    print(response.json())
    assert response.status_code == 200

    customer_model = CustomerResponse(**response.json())
    assert customer_model.id.startswith('cus')
    assert customer_model.name == 'Doe'
