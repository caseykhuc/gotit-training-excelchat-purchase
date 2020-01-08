import enum


class Url(enum.Enum):
    ADMIN = "http://admin.got-it.io/"
    GET_SUBSCRIPTION = "https://api.got-it.io/admin/askers/16413/subscriptions"
    TERMINATE = "https://api.got-it.io/admin/askers/16413/subscriptions/{}"
    ASKER_URL = "http://www.got-it.io/solutions/excel-chat"


class AskerAccount(enum.Enum):
    EMAIL = "trang+02@gotitapp.co"
    PASSWORD = "1234aA"
    DEFAULT_CARD = "1881"


class AdminAccount(enum.Enum):
    ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6ImJjMzMwZjkxIiwiaWF0IjoxNTc4NDU1MTA1LCJzdWIiOjEwMCwiZXhwIjoxNjA5OTkxMTA1LCJhdWQiOiJhZG1pbiJ9.U-mgnyM4dCpK0ga4J1lWstXdQkygnw8Hxp_lmVJhgFk"
