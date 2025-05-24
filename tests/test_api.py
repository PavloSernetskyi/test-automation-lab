import requests  # Import the requests library for making HTTP requests

def test_get_posts():
    # Send a GET request to the API endpoint
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    # Assert that the response status code is 200 (OK)
    assert res.status_code == 200
    # Assert that the response body is a list (of posts)
    assert isinstance(res.json(), list)