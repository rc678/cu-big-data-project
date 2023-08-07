from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# How to run test: python -m pytest tests
# https://stackoverflow.com/questions/20985157/py-test-no-module-named
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
