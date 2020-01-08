import requests
import json
from config.main import Url, AdminAccount


class CleanUp:
    _headers = {
        "Authorization": "Bearer {}".format(AdminAccount.ACCESS_TOKEN.value),
        "Content-Type": "application/json",
        "x-gotit-vertical": "Excel",
    }

    def terminate_subscription(self):
        subscription_id = self.get_subscription_id()
        url = Url.TERMINATE.value.format(subscription_id)
        payload = {"status": "terminated", "product": "excelchat"}
        response = requests.put(
            url, params={"product": "excelchat"}, json=payload, headers=self._headers,
        )

    def get_subscription_id(self):
        url = Url.GET_SUBSCRIPTION.value
        payload = {}
        response = requests.get(
            url,
            params={"product": "excelchat"},
            data=json.dumps(payload),
            headers=self._headers,
        )
        return json.loads(response.text)["data"]["latest_subscription"]["id"]
