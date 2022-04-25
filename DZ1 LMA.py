import requests
import time
import json
from pprint import pprint

def git_data(url):
    response = requests.get(url)
    return response.json()

username = input('Введите username: ')
url = f"https://api.github.com/users/{username}/repos"

response = git_data(url)
#pprint(response)

repozits = []
for i in response:
    repozits.append(i['name'])
print(f'Репозитории {username}')
print(repozits)

with open('repozits.json', 'w') as f:
    json_repozits = json.dump(repozits, f)