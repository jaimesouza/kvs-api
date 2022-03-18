from fastapi.testclient import TestClient
from kvs import app


client = TestClient(app)


class TestAPI:

    def test_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}
