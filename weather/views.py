from requests.api import post
import weather
from django.shortcuts import render
import requests
from .models import *
from .forms import CityForm
def index(request):
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        if form.is_valid():
            city = form.cleaned_data['name']
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=2fded949492787e9e7a95573c7a75f18'
            city_weather = requests.get(url.format(city)).json()
            weather = {
                'city': city,
                'temperature': city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon'],
                }
            context={
                'weather': weather,
                }
            return render(request, 'weather/index.html',context)
    else:
        form = CityForm()
        return render(request, 'weather/index.html')
    
    
    
