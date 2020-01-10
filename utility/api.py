import requests
import json


class ApiRequest:
    _default_header = {
        "Authorization": "Bearer {}",
        "x-gotit-vertical": "Excel",
    }
    _default_params = {"product": "excelchat"}
    _default_payload = {}

    @staticmethod
    def with_content_type(_headers):
        headers = _headers
        headers["Content-Type"] = "application/json"
        return headers

    @staticmethod
    def with_admin_account(_headers, admin_account):
        headers = _headers
        headers["Authorization"] = _headers["Authorization"].format(
            admin_account.ACCESS_TOKEN.value
        )
        return headers

    @staticmethod
    def put(url, admin_account, params=_default_params, payload=_default_payload):
        headers = ApiRequest.with_content_type(ApiRequest._default_header)
        headers = ApiRequest.with_admin_account(headers, admin_account)
        return requests.put(url, params=params, json=payload, headers=headers,)

    @staticmethod
    def post(url, admin_account, params=_default_params, payload=_default_payload):
        headers = ApiRequest.with_content_type(ApiRequest._default_header)
        headers = ApiRequest.with_admin_account(headers, admin_account)
        return requests.post(url, params=params, json=payload, headers=headers,)

    @staticmethod
    def get(url, admin_account, params=_default_params):
        headers = ApiRequest.with_admin_account(
            ApiRequest._default_header, admin_account
        )
        return requests.get(url, params=params, headers=headers)


class ApiResponse:
    def get_loaded_response(response):
        return json.loads(response)
