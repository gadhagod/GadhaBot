import requests
import os
import city as citydb

def CtoF(C):
    F = (C * (9/5)) + 32
    F = round(F, 2)
    return F

def findweather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, os.environ.get('WEATHER_SECRET'))
    req = requests.get(url)
    print(req)
    info = req.json()

    Ctemp = info['main']['temp']
    Cfeels_like = info['main']['feels_like']
    humidity = info['main']['humidity']
    description = info['weather'][0]['description']
    Cmintemp = info['main']['temp_min']
    Cmaxtemp = info['main']['temp_max']

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


def weather(userid):
    print('Weather query')
    city = citydb.get(userid)
    if city == '':
        return(False)
    else:
        return(findweather(city))
