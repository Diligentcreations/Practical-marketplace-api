from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "JUT Marketplace API is running"

def test_get_professionals():
    client = app.test_client()
    response = client.get("/professionals")
    assert response.status_code == 200
    assert len(response.json) == 3

def test_professional_not_found():
    client = app.test_client()
    response = client.get("/professionals/999")
    assert response.status_code == 404
