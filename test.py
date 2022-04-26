import requests
import pytest

user_id = '2818'
base_url = "https://gorest.co.in/"


def test_valid_url():
    url = base_url + "/public/v2/users/" + user_id
    response = requests.get(url)
    assert response.status_code == 200


def test_valid_data():
    url = base_url + "/public/v2/users/" + user_id
    name = 'Tanirika Mahajan'
    email = 'tanirika_mahajan@wisozk-kreiger.name'
    status = 'inactive'
    response = requests.get(url)
    json = response.json()
    assert name == json['name']
    assert email == json['email']
    assert status == json['status']
