import time

import pytest
import requests

BASE_URL = "http://localhost:5000"


@pytest.fixture
def auth_token():
    user_data = {
        "username": f"dirk{int(time.time() * 1000)}",
        "password": "super_secure_pw"
    }
    requests.post(f"{BASE_URL}/api/auth/register", json=user_data)
    response = requests.post(f"{BASE_URL}/api/auth/login", json=user_data)
    return response.json()["access_token"]