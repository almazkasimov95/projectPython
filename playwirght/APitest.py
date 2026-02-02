import requests

def test_get_post_by_id():
    post_id = 1
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()

    required_fields = ["userId", "title", "body", 'id']
    for field in required_fields:
        assert field in data, f"{field} is missing"

    assert data["userId"] == post_id