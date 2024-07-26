from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
# Create your views here.
from django.views.generic.base import TemplateView
import requests

# Create Home View
class HomeView(TemplateView):

  template_name = 'weather/home.html'
  success_url = reverse_lazy('home')


def weather_view(request):

    if request.method == 'GET' and 'lat' in request.GET and 'lon' in request.GET:
        lat = request.GET['lat']
        lon = request.GET['lon']
        api_key = '3b333984ea5d121b4046f326ff6b1897'  # Replace with your OpenWeatherMap API key
        units = 'metric'
        lang = 'fr'
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}&lang={lang}'
        response = requests.get(url)
    
        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Unable to fetch weather data'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method or missing coordinates'}, status=400)


def space_view(request):

    # Get API data
    api_key = "ODssD8zAvr10XyJxGBRCvOeh6Q7WXWzwaYilGyTG"
    url = f"https://api.nasa.gov/planetary/apod?count=6&api_key={api_key}"

    nasa_data = requests.get(url.format(api_key)).json() # Request the API data and convert the JSON to Python data types

    #

    photos = []
    for data in nasa_data:
        #print(data['url'])
        photos.append({
            'url': data['url'],
        })

 #

    # Return context to home page
    context = {
        'photos': photos,
    }
    return render(request, 'weather/space.html', context)