from enum import Enum


class EnvEnums(Enum):
    ORG_ID: str = "ORG_ID"
    BASE_URL: str = "BASE_URL"
    AUTH_URL: str = "AUTH_URL"
    API_URL: str = "API_URL"
    API_KEY: str = "API_KEY"
    API_SECRET: str = "API_SECRET"
    MFA_SECRET_KEY: str = "MFA_SECRET_KEY"
    EMAIL: str = "EMAIL"
    PASSWORD: str = "PASSWORD"
