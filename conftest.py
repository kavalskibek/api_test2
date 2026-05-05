import os
import pytest
from dotenv import load_dotenv
from api_helper import StripeAPI

load_dotenv()



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