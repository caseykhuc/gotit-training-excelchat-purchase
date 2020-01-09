from config.main_config import Url, AdminAccount
from utility.api import ApiRequest, ApiResponse


class CleanUp:
    def terminate_subscription(self):
        subscription_id = self.get_subscription_id()
        ApiRequest.put(
            Url.TERMINATE.value.format(subscription_id),
            payload={"status": "terminated", "product": "excelchat"},
        )

    def get_subscription_id(self):
        response = ApiRequest.get(Url.GET_SUBSCRIPTION.value)
        return ApiResponse.get_loaded_response(response.text)["data"][
            "latest_subscription"
        ]["id"]
