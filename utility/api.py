import requests
import json


class ApiRequest:
    _default_header = {
        "x-gotit-vertical": "Excel",
    }
    _default_params = {"product": "excelchat"}
    _default_payload = {}

    _content_type_header = {"Content-Type": "application/json"}

    @staticmethod
    def request(
        method, url, params=_default_params, payload=_default_payload, headers={},
    ):
        """ Utility method to create API request
        
        Parameters:
        method (str): request method (get / put / post)
        url (str)
        params (dict)
        payload (dict)
        headers (dict): Additional headers
        
        """
        complete_headers = ApiRequest._default_header
        complete_headers.update(headers)

        if method == "get":
            return requests.get(url, params=params, headers=complete_headers)

        if method == "put":
            return requests.put(
                url, params=params, json=payload, headers=complete_headers
            )

        if method == "post":
            return requests.post(
                url, params=params, json=payload, headers=complete_headers,
            )

    def get(url, headers):
        return ApiRequest.request("get", url, headers=headers,)

    def put(url, headers, payload):
        headers.update(ApiRequest._content_type_header)
        return ApiRequest.request("put", url, payload=payload, headers=headers)

    def post(url, headers, payload):
        headers.update(ApiRequest._content_type_header)
        return ApiRequest.request("post", url, payload=payload, headers=headers)


class ApiResponse:
    def get_loaded_response(response):
        return json.loads(response)
