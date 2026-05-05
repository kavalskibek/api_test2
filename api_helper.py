import requests


class StripeAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url, headers=self.headers)
        return response  # ← не забудь return

    def post(self, endpoint, data):
        url = f'{self.base_url}/{endpoint}'
        response = requests.post(url, data=data, headers=self.headers)
        return response


    def delete(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = requests.delete(url, headers=self.headers)
        return response
