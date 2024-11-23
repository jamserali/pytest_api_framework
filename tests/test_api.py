class TestAPI:

    def tes_get_request_success(self, api_client, default_headers):
        params = {"name": "John", "age": 30, "city": "New York"}
        response = api_client.get("/", params=params, headers=default_headers)
        print(response)

        assert response.status_code == 200
        # json_data = response.json()
        # assert json_data["success"] is True
        # assert json_data["data"] == {"name":"John","age":30,"city":"New York"}

    def test_get_all_products(self, api_client, default_headers):
        params = {"name": "John", "age": 30, "city": "New York"}
        response = api_client.get("/products", params=params, headers=default_headers)
        prod = response.json()
        print(prod['products'][0]['id'])
        print(len(prod['products']))
        print(prod['products'][1]['title'])
        # print(prod['products'])
        assert response.status_code == 200
        # Lists of assertion in API Testing
        # assert 'next' in response.json()
        # assert response.json()['page'] == 1
        # assert len(response.json()) == len(set(item['id'] for item in response.json()))
        # assert response.json() == expected_data
        # assert 'error' in response.json()
        # assert response.json()['error']['message'] == 'Invalid input'
        assert response.headers['X-RateLimit-Remaining'] == '99'
        assert 'X-RateLimit-Limit' in response.headers
        assert response.elapsed.total_seconds() < 2  # Response time should be less than 2 seconds
        # assert response.json()['id'] == expected_id
        assert response.json()['products'][0]['availabilityStatus'] == 'Low Stock'
        # assert 'id' in response.json()
        assert isinstance(response.json()['products'][0]['title'], str)
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        # assert response.status_code == 200  # OK
        # assert response.status_code == 201  # Created
        # assert response.status_code == 204  # No Content
        # assert response.status_code == 400  # Bad Request
        # assert response.status_code == 401  # Unauthorized
        # assert response.status_code == 403  # Forbidden
        # assert response.status_code == 404  # Not Found
        # assert response.status_code == 500  # Internal Server Error















