from fastapi.testclient import TestClient

import main
client = TestClient(main.app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Hello there.."}

def test_read_main():
    response = client.post("/predict")
    assert response.status_code == 200
    assert response.json() == {"message": "hello from prediction."}