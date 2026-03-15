import os

import pytest
from dotenv import load_dotenv
load_dotenv()

@pytest.fixture(scope="session")
def configs():
    return {
        "base_url": os.getenv('BASE_URL'),
        "login_url": os.getenv('LOGIN_URL'),
        "username": os.getenv('USERNAME'),
        "email": os.getenv('EMAIL'),
        "invalid_email": os.getenv('INVALID_EMAIL'),
        "password": os.getenv('PASSWORD'),
        "invalid_password": os.getenv('INVALID_PASSWORD')
    }