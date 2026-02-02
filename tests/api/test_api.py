# test/test_api.py
import requests

def test_get_post_by_id(api_base_url):
    post_id = 1
    url = f"{api_base_url}/posts/{post_id}"

    # Act
    response = requests.get(url)

    # Assert
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["id"] == post_id
    assert "title" in json_data
    assert "body" in json_data
    assert json_data["id"] == 1


def test_create_post():
    url = f"https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Test Post",
        "body": "This is a test post",
        "user_id": 1
    }
    response = requests.post(url, json=payload)

    assert response.status_code == 201 # Created
    json_data = response.json()
    assert json_data["title"] == "Test Post"
    assert json_data["body"] == "This is a test post"
    assert json_data["user_id"] == 1
    assert "id" in json_data # сервер присваивает ID