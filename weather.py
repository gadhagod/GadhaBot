import requests
import os

def weather(city):
    if city == '':
        return 'Please specify city.'
    else:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, os.environ.get('WEATHER_SECRET'))
        req = requests.get(url)
        data = req.json()

        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        mintemp = data['main']['temp_min']
        maxtemp = data['main']['temp_max']

        strdescription = 'Status: ' + str(description) + '\n'
        strtemp = 'Current temperature: ' + str(temp) + '°C\n'
        strfeels_like = 'Feels like: ' + str(feels_like) + '°C\n'
        strmaxtemp = 'Today\'s high: ' + str(maxtemp) + '°C\n'
        strmintemp = 'Today\'s low: ' + str(mintemp) + '°C\n'
        strhumidity = 'Humidity: ' + str(humidity) + '%'


        return strdescription, strtemp, strfeels_like, strmaxtemp, strmintemp, strhumidity
