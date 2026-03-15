import os
from dataclasses import dataclass

import pytest
from dotenv import load_dotenv
load_dotenv()

@dataclass(frozen=True)
class Config:
    base_url: str
    login_url: str
    username: str
    email: str
    invalid_email: str
    password: str


@pytest.fixture(scope="session")
def configs():
    return Config(
        base_url=os.getenv('BASE_URL'),
        login_url=os.getenv('LOGIN_URL'),
        username=os.getenv('USERNAME'),
        email=os.getenv('EMAIL'),
        invalid_email=os.getenv('INVALID_EMAIL'),
        password=os.getenv('PASSWORD'),
    )