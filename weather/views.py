from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_protect
from .models import City
from .forms import CityForm


@csrf_protect
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    
    # new_city = request.form.get('city')
    # new_city = 'Nairobi'

    cities = City.objects.all()

    api_key = 'a778d9642410a11ed2cbd17c20c246bc'
    
    
    # print( response)
    form = CityForm()
    weather_data = []

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    else:
        form = CityForm()
        

    for new_city in cities:
        response = requests.get(url.format(new_city, api_key)).json()


        weather = {
            'city' : new_city,
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
            'pressure' : response['main']['pressure']
            
        }

        weather_data.append(weather)

    context = {
        'weather' : weather_data,
        'form' : form
    }

    return render(request, 'index.html', context)