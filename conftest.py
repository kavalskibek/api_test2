import os
import pytest
from dotenv import load_dotenv
from api_helper import StripeAPI
from faker import Faker
load_dotenv()



@pytest.fixture
def fake():
    return Faker()

@pytest.fixture
def customer_payload_factory(fake):
    def _factory(**overrides):
        payload = {
            "email": fake.email(),
            "name": fake.name(),
            "description": "Created by API automation test"
        }

        payload.update(overrides)
        return payload

    return _factory

@pytest.fixture
def created_customer(stripe_api, customer_payload_factory):
    payload = customer_payload_factory()

    create_response = stripe_api.post("customers", data=payload)
    assert create_response.status_code == 200

    customer = create_response.json()
    customer_id = customer["id"]

    yield customer

    delete_response = stripe_api.delete(f"customers/{customer_id}")
    assert delete_response.status_code == 200


@pytest.fixture(scope='session')
def api_headers():
    key = os.getenv('STRIPE_SECRET_KEY')
    return {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

@pytest.fixture(scope='session')
def base_url():
    return "https://api.stripe.com/v1"


@pytest.fixture(scope='session')
def stripe_api(api_headers, base_url):
    return StripeAPI(base_url, api_headers)