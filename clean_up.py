import requests
import json
from config.main import Url, AdminAccount


class CleanUp:
    _headers = {
        "Authorization": "Bearer %s" % str(AdminAccount.ACCESS_TOKEN.value),
        "Content-Type": "application/json",
        "x-gotit-vertical": "Excel",
    }

    def terminate_subscription(self):
        subscription_id = self.get_subscription_id()
        url = str(Url.TERMINATE.value) % str(subscription_id)
        payload = {"status": "terminated", "product": "excelchat"}
        response = requests.put(
            url, params={"product": "excelchat"}, json=payload, headers=self._headers,
        )

    def get_subscription_id(self):
        url = str(Url.GET_SUBSCRIPTION.value)
        payload = {}
        response = requests.get(
            url,
            params={"product": "excelchat"},
            data=json.dumps(payload),
            headers=self._headers,
        )
        return json.loads(response.text)["data"]["latest_subscription"]["id"]
