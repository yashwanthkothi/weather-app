import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_weather_endpoint(client, monkeypatch):
    # Mock the API response
    mock_response = {
        "main": {
            "temp": 15.5
        }
    }
    
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.status_code = 200
            def json(self):
                return mock_response
            def raise_for_status(self):
                pass
        return MockResponse()
    
    monkeypatch.setattr("requests.get", mock_get)
    
    response = client.get('/')
    assert response.status_code == 200
    assert b"Weather in London: 15.5" in response.data

def test_weather_endpoint_failure(client, monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.exceptions.RequestException("API Error")
    
    monkeypatch.setattr("requests.get", mock_get)
    
    response = client.get('/')
    assert response.status_code == 500
    data = json.loads(response.data)
    assert "error" in data
