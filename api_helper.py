import requests
import uuid
from loguru import logger



logger.add("allure-results/api_logs.json", format="{message}", serialize=True, rotation="5 MB")


class StripeAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def _send_request(self, method: str, endpoint: str, data=None):

        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        trace_id = str(uuid.uuid4())


        req_logger =logger.bind(
            trace_id=trace_id,
            method=method,
            endpoint=url,
            payload=data
        )

        req_logger.info(f'==> Send {method} request to {url}')

        response = requests.request(method, url, headers=self.headers, data=data)

        try:
            resp_body = response.json()
        except ValueError:
            resp_body = response.text


        res_logger = req_logger.bind(
            status_code=response.status_code,
            response_time_ms = int(response.elapsed.total_seconds() * 1000),
            response_body=resp_body,

        )

        if response.ok:
            res_logger.info(f"<== Успешный ответ {response.status_code}")
        else:
            res_logger.error(f"<== Ошибка API {response.status_code}")

        return response

    def get(self, endpoint):
        return self._send_request('GET', endpoint)

    def post(self, endpoint, data):
        return self._send_request('POST', endpoint, data=data)

    def delete(self, endpoint):
        return self._send_request('DELETE', endpoint)

    def delete_customer(self, customer_id):
        return self.delete(f'customers/{customer_id}')