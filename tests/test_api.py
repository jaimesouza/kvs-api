from fastapi.testclient import TestClient
from kvs import app


client = TestClient(app)


class TestAPI:

    def test_root(self):

        expected_json = {
            "Name": "Key-Value Store REST API",
            "Author": "Jaime Freire"
        }

        response = client.get("/")

        assert response.status_code == 200
        assert response.json() == expected_json
        assert response.headers["app-name"] == "kvs-api"
        assert response.headers["app-author"] == "Jaime Freire"

    def test_fetch_pairs(self):

        expected_json = [
            {
                "key": "id",
                "value": "ID001"
            },
            {
                "key": "name",
                "value": "Jon Snow"
            },
            {
                "key": "serie",
                "value": "Game of Thrones"
            }
        ]

        response = client.get("/api/pairs")

        assert response.status_code == 200
        assert response.json() == expected_json

    def test_fetch_value(self):

        expected_json = {
            "key": "name",
            "value": "Jon Snow"
        }

        response = client.get("/api/pairs/name")

        assert response.status_code == 200
        assert response.json() == expected_json

    def test_fetch_value_nonexistent_key(self):

        expected_json = {
            "detail": "key name1 does not exist"
        }

        response = client.get("/api/pairs/name1")

        assert response.status_code == 404
        assert response.json() == expected_json

    def test_insert_pair(self):

        expected_json = {
            "key": "region",
            "value": "North"
        }

        response = client.post(
            "/api/pairs",
            json=expected_json,
        )

        assert response.status_code == 201
        assert response.json() == expected_json

    def test_insert_pair_existing_key(self):

        expected_json = {
            "detail": "key name already exists"
        }

        response = client.post(
            "/api/pairs",
            json={
                "key": "name",
                "value": "Stark"
            }
        )

        assert response.status_code == 409
        assert response.json() == expected_json

    def test_update_pair(self):

        expected_json = {
            "key": "name",
            "value": "Ned Stark"
        }

        response = client.put(
            "/api/pairs/name",
            json={"value": "Ned Stark"}
        )

        assert response.status_code == 201
        assert response.json() == expected_json

    def test_update_pair_nonexistent_key(self):

        expected_json = {
            "detail": "key test does not exist"
        }

        response = client.put(
            "/api/pairs/test",
            json={"value": "New value"}
        )

        assert response.status_code == 404
        assert response.json() == expected_json

    def test_delete_pair(self):

        expected_json = {
            "key": "id",
            "value": "ID001"
        }

        response = client.delete("/api/pairs/id")

        assert response.status_code == 200
        assert response.json() == expected_json

    def test_delete_pair_nonexistent_key(self):

        expected_json = {
            "detail": "key test does not exist"
        }

        response = client.delete("/api/pairs/test")

        assert response.status_code == 404
        assert response.json() == expected_json

    def test_integration(self):

        # delete all key-value pairs
        client.delete("/api/pairs/id")
        client.delete("/api/pairs/name")
        client.delete("/api/pairs/serie")
        client.delete("/api/pairs/region")

        # insert a new key-value pair
        client.post(
            "/api/pairs",
            json={
                "key": "age",
                "value": "30"
            }
        )

        # insert a new key-value pair
        client.post(
            "/api/pairs",
            json={
                "key": "country",
                "value": "Brazil"
            }
        )

        # update one key-value pair
        client.put(
            "/api/pairs/country",
            json={"value": "USA"}
        )

        # delete one key-value pair
        client.delete("/api/pairs/age")

        # fetch all key-value pairs
        response = client.get("/api/pairs")

        expected_json = [
            {
                "key": "country",
                "value": "USA"
            }
        ]

        assert response.status_code == 200
        assert response.json() == expected_json

        # delete one key-value pair
        client.delete("/api/pairs/country")

        # fetch all key-value pairs
        response = client.get("/api/pairs")

        assert response.status_code == 200
        assert response.json() == []
