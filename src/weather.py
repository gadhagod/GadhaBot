import requests
import os

def CtoF(C):
    F = (C * (9/5)) + 32
    F = round(F, 2)
    return F

def weather(city):
    print('Weather query')
    if city == '':
        return 'Please specify city.'
    else:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, os.environ.get('WEATHER_SECRET'))
        req = requests.get(url)
        data = req.json()

        Ctemp = data['main']['temp']
        Cfeels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        Cmintemp = data['main']['temp_min']
        Cmaxtemp = data['main']['temp_max']

        Ftemp = CtoF(float(Ctemp))
        Ffeels_like = CtoF(float(Cfeels_like))
        Fmintemp = CtoF(float(Cmintemp))
        Fmaxtemp = CtoF(float(Cmaxtemp))

        strdescription = 'Status: ' + str(description) + '\n'
        strtemp = 'Current temperature: ' + str(Ctemp) + '°C, ' + str(Ftemp) + '°F\n'
        strfeels_like = 'Feels like: ' + str(Cfeels_like) + '°C, ' + str(Ffeels_like) + '°F\n'
        strmaxtemp = 'Today\'s high: ' + str(Cmaxtemp) + '°C, ' + str(Fmaxtemp) + '°F\n'
        strmintemp = 'Today\'s low: ' + str(Cmintemp) + '°C, ' + str(Fmintemp) + '°F\n'
        strhumidity = 'Humidity: ' + str(humidity) + '%'

        return strdescription, strtemp, strfeels_like, strmaxtemp, strmintemp, strhumidity
