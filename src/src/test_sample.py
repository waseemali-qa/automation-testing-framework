# src/test_sample.py

import requests

def test_google_homepage():
    """Test to check the status code of Google homepage"""
    response = requests.get("https://www.google.com")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

def test_api_endpoint():
    """Test to verify a sample API endpoint"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    assert "userId" in response.json(), "userId not found in response"
