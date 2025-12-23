from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

#Test cases for loan eligibility endpoint
def test_eligibility_pass():
    payload = {
        "income": 60000,
        "age": 30,
        "employment_status": "employed"
    }
    response = client.post("/loan-eligibility/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"eligible": True}

def test_eligibility_fail():
    payload = {
        "income": 30000,
        "age": 18,
        "employment_status": "unemployed"
    }
    response = client.post("/loan-eligibility/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"eligible": False}