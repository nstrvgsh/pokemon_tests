import requests

TOKEN = '7d9ec145fad8f1fbb748142052d96ac9'
URL = 'https://api.pokemonbattle.ru/v2'
headers = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}

# 1. Создание покемона
create_response = requests.post(
    f'{URL}/pokemons',
    headers=headers,
    json={
        "name": "generate",
        "photo_id": -1
    }
)

data = create_response.json()
print("Статус код:", create_response.status_code)
print("Ответ:", data)

# 2. Смена имени покемона
rename_response = requests.patch(
    f'{URL}/pokemons',
    headers=headers,
    json={
        "pokemon_id": data['id'],
        "name": "generate",
    }
)

rename_data = rename_response.json()
print("Статус код:", rename_response.status_code)
print("Ответ:", rename_data)
catch_response = requests.post(
    f'{URL}/trainers/add_pokeball',
    headers=headers,
    json={
        "pokemon_id": data['id']
    }
)

catch_data = catch_response.json()
print("Статус код:", catch_response.status_code)
print("Ответ:", catch_data)