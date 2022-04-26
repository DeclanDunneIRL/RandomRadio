from django.http import JsonResponse
from django.shortcuts import render
from django.core.cache import cache
import requests
import json
import random



url = "https://de1.api.radio-browser.info/json/stations/bylanguage/english"

# Return the json from the api url
def get_json():
    response = requests.get(url)
    return json.loads(response.text)
	
# Cache the stations and get another random one
def get_random_station(request):
    stations = cache.get('stations')
    if stations is None:
        stations = get_json()
        cache.set('stations', stations)
    station = stations[random.randint(0, len(stations)-1)]
    return render(request, 'index.html', {'station': station})





