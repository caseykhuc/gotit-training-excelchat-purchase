import enum


class Url(enum.Enum):
    ADMIN = "http://admin.got-it.io/"
    GET_SUBSCRIPTION = "https://api.got-it.io/admin/askers/16413/subscriptions"
    TERMINATE = "https://api.got-it.io/admin/askers/16413/subscriptions/%s"
    ASKER_URL = "http://www.got-it.io/solutions/excel-chat"


class AskerAccount(enum.Enum):
    EMAIL = "trang+01@gotitapp.co"
    PASSWORD = "1234aA"


class AdminAccount(enum.Enum):
    """ EMAIL = "trang@gotitapp.co"
    PASSWORD = "xoxoFire" """

    ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6ImJjMzMwZjkxIiwiaWF0IjoxNTc4NDU1MTA1LCJzdWIiOjEwMCwiZXhwIjoxNjA5OTkxMTA1LCJhdWQiOiJhZG1pbiJ9.U-mgnyM4dCpK0ga4J1lWstXdQkygnw8Hxp_lmVJhgFk"
