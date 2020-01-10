from utility.api import ApiRequest, ApiResponse


class CleanUp:
    def terminate_subscription(self, Url, AdminAccount):
        subscription_id = self.get_subscription_id(Url, AdminAccount)
        ApiRequest.put(
            Url.TERMINATE.value.format(subscription_id),
            AdminAccount,
            payload={"status": "terminated", "product": "excelchat"},
        )

    def get_subscription_id(self, Url, AdminAccount):
        response = ApiRequest.get(Url.GET_SUBSCRIPTION.value, AdminAccount)
        return ApiResponse.get_loaded_response(response.text)["data"][
            "latest_subscription"
        ]["id"]
