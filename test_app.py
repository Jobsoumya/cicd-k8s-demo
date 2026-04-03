import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"CI/CD Pipeline Demo" in response.data


def test_form_submission(client):
    response = client.post("/", data={"username": "Soumya"})
    assert response.status_code == 200
    assert b"Hello Soumya" in response.data
