# File: backend/test_main.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_valid_split():
    response = client.post("/validate-split", json={
        "total": 100,
        "splits": {"Alice": 50, "Bob": 50}
    })
    assert response.status_code == 200
    assert response.json() == {"valid": True, "message": "Split is valid"}

def test_invalid_split():
    response = client.post("/validate-split", json={
        "total": 100,
        "splits": {"Alice": 60, "Bob": 30}
    })
    assert response.status_code == 200
    assert response.json()["valid"] is False
    assert "Split does not match" in response.json()["message"]

def test_zero_total():
    response = client.post("/validate-split", json={
        "total": 0,
        "splits": {"Alice": 0, "Bob": 0}
    })
    assert response.status_code == 422  # Fails validation from pydantic

def test_missing_fields():
    response = client.post("/validate-split", json={})
    assert response.status_code == 422
