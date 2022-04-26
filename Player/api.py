from rest_framework import viewsets, permissions

from . import serializers
from . import models

# # Return the json from the api url
# def get_json():
#     import requests
#     import json
#     response = requests.get(url)
#     return json.loads(response.text)

# # Select a random station from the json
# def get_random_station():
#     import random
#     json = get_json()
#     print(json[random.randint(0, len(json)-1)])