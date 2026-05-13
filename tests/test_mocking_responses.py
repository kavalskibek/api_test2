import pytest
import responses
from requests.exceptions import ReadTimeout

@responses.activate
def test_create_customer_stripe_timeout(stripe_api):
    target_url = f"{stripe_api.base_url.rstrip('/')}/customers"

    responses.add(
        responses.POST,
        target_url,
        body=ReadTimeout('Stripe API is hanging!')
    )

    data = {
        'email': 'timeout@gmail.com',
        'name': 'Timeout User'
    }

    with pytest.raises(ReadTimeout):
        stripe_api.post('customers', data=data)

    
# @responses.activate
# def test_create_customer_stripe_500_error(stripe_api):
#     target_url = f"{stripe_api.base_url.rstrip('/')}/customers"
#     responses.add(
#         responses.POST,
#         target_url,
#         json={'error': {'message': 'Stripe is completely down!'}},
#         status=500,
#     )
# 
# 
#     data = {
#         'email': 'mockuser@gmail.com',
#         'name': 'Mock User',
#     }
# 
# 
#     response = stripe_api.post('customers', data = data)
#     assert response.status_code == 500
#     assert response.json()["error"]["message"] == "Stripe is completely down!"