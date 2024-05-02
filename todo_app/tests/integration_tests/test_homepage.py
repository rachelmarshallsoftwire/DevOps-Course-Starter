import requests
from config import client, stub


def test_index_page(monkeypatch, client):
     # This replaces any call to requests.get with our own function
    monkeypatch.setattr(requests, 'get', stub)

    response = client.get('/')

    assert response.status_code == 200
    assert 'Test card' in response.data.decode()