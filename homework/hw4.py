from http.client import responses

import requests  #импортируем библиотеку requests

response = requests.get("https://api.github.com") # отправляем запрос на github

print(response.json())
#выводит ответ, который вернет на github, информация о сервере

