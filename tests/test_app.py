import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_for_activity():
    # Get an activity name
    activities = client.get("/activities").json()
    activity_name = next(iter(activities))
    email = "testuser@mergington.edu"
    # Sign up
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code == 200 or response.status_code == 400
    # Try duplicate signup
    response_dup = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response_dup.status_code == 400
    assert "already signed up" in response_dup.json()["detail"].lower()

