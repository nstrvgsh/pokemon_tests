import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TRAINER_ID = USER_ID
EXPECTED_TRAINER_NAME = 'TRAINER_NAME'

def test_status_code():
    response = requests.get(f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_name_in_response():
    response = requests.get(f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    trainer = response.json()['data'][0]
    assert trainer['trainer_name'] == EXPECTED_TRAINER_NAME
