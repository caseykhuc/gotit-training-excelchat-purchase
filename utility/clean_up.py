from utility.api import ApiRequest, ApiResponse


class CleanUp:
    def terminate_subscription(self, Url, AdminAccount):
        auth_header = {"Authorization": "Bearer {}".format(AdminAccount.ACCESS_TOKEN)}
        subscription_id = self.get_subscription_id(Url, AdminAccount)

        ApiRequest.put(
            Url.TERMINATE.format(subscription_id),
            payload={"status": "terminated", "product": "excelchat"},
            headers=auth_header,
        )

    def get_subscription_id(self, Url, AdminAccount):
        auth_header = {"Authorization": "Bearer {}".format(AdminAccount.ACCESS_TOKEN)}
        response = ApiRequest.get(Url.GET_SUBSCRIPTION, headers=auth_header,)

        return ApiResponse.get_loaded_response(response.text)["data"][
            "latest_subscription"
        ]["id"]
