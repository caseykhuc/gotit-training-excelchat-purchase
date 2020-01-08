import requests
import json
from config.main_config import Url, AdminAccount


class ApiRequest:
    _default_header = {
        "Authorization": "Bearer {}".format(AdminAccount.ACCESS_TOKEN.value),
        "x-gotit-vertical": "Excel",
    }
    _default_params = {"product": "excelchat"}
    _default_payload = {}

    @staticmethod
    def with_content_type():
        header = ApiRequest._default_header
        header["Content-Type"] = "application/json"
        return header

    @staticmethod
    def put(url, params=_default_params, payload=_default_payload):
        return requests.put(
            url, params=params, json=payload, headers=ApiRequest.with_content_type(),
        )

    @staticmethod
    def post(url, params=_default_params, payload=_default_payload):
        return requests.post(
            url, params=params, json=payload, headers=ApiRequest.with_content_type(),
        )

    @staticmethod
    def get(url, params=_default_params):
        return requests.get(url, params=params, headers=ApiRequest._default_header)


class ApiResponse:
    def get_loaded_response(response):
        return json.loads(response)
