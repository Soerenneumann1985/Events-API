import requests
import time

def test_health_check():

    response = requests.get("http://localhost:5000/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_register_user():

    user_data = {
        "username": f"dirk{int(time.time()*1000)}",
        "password": "super_secure_pw"
    }

    response = requests.post("http://localhost:5000/api/auth/register",
                    json=user_data)

    print(response.json())
    assert response.status_code == 201
    assert response.json()["user"]["username"] == user_data["username"]


def test_login_returns_jwt_token():
    user_data = {
        "username": f"dirk{int(time.time() * 1000)}",
        "password": "super_secure_pw"
    }

    requests.post("http://localhost:5000/api/auth/register", json=user_data)

    response = requests.post("http://localhost:5000/api/auth/login", json=user_data)

    print(response.json())
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_create_public_event(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}

    event_data = {
        "title": "Test Event",
        "description": "Event aus dem automatisierten Test",
        "date": "2027-01-15T18:00:00",
        "is_public": True,
        "requires_admin": False
    }

    response = requests.post(
        "http://localhost:5000/api/events",
        json=event_data,
        headers=headers
    )

    assert response.status_code == 201
    assert response.json()["title"] == event_data["title"]


def test_rsvp_to_public_event(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}

    # 1. öffentliches Event anlegen (wie im letzten Test)
    event_data = {
        "title": "Test Event RSVP",
        "description": "Event aus dem automatisierten Test",
        "date": "2027-01-15T18:00:00",
        "is_public": True,
        "requires_admin": False
    }
    event_response = requests.post("http://localhost:5000/api/events",
                                   json=event_data, headers=headers)
    event_id = event_response.json()["id"]

    # 2. zusagen
    response = requests.post(
        f"http://localhost:5000/api/rsvps/event/{event_id}",
        json={"attending": True}
    )

    print(response.json())
    assert response.status_code == 201

def test_create_event_without_token_fails():
    event_data = {
            "title": "Event ohne Token",
            "description": "Sollte nicht klappen",
            "date": "2027-01-15T18:00:00",
            "is_public": True,
            "requires_admin": False
        }

    response = requests.post("http://localhost:5000/api/events", json=event_data)

    assert response.status_code == 401

def test_duplicate_registration_fails():
    user_data = {
        "username": f"dirk{int(time.time() * 1000)}",
        "password": "super_secure_pw"
    }

    requests.post("http://localhost:5000/api/auth/register", json=user_data)

    response = requests.post("http://localhost:5000/api/auth/register", json=user_data)

    assert response.status_code == 400

def test_rsvp_to_protected_event_without_token_fails(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}

    event_data = {
        "title": "Protected Test Event",
        "description": "Nur mit Login",
        "date": "2027-01-15T18:00:00",
        "is_public": False,
        "requires_admin": False
    }

    event_response = requests.post(
        "http://localhost:5000/api/events",
        json=event_data,
        headers=headers
    )
    event_id = event_response.json()["id"]

    response = requests.post(
        f"http://localhost:5000/api/rsvps/event/{event_id}",
        json={"attending": True}
    )

    assert response.status_code == 401