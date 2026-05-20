from faker import Faker


def test_customer_payload_factory_can_override_email(customer_payload_factory):
    payload = customer_payload_factory(email="wrong-email")
    print(payload)

    assert payload["email"] == "wrong-email"
    assert "name" in payload
    assert "description" in payload

def test_customer_payload_factory_default_data(customer_payload_factory):
    payload = customer_payload_factory()

    print(payload)


    assert '@' in payload['email']
    assert len(payload['name']) > 0
    assert payload["description"] == "Created by API automation test"