import pyowm, os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import api_keys as api

def getString(location):

    weatherAr = getCurrentWeather(location);

    windDirection = int(round(weatherAr['wind'][u'deg']))
    currentTemp   = int(round(weatherAr['temperature']['temp']))
    windSpeed     = int(round(weatherAr['wind'][u'speed']))
    humidity      = int(round(weatherAr['humidity']))
    maxTemp       = int(round(weatherAr['temperature']['temp_max']))
    minTemp       = int(round(weatherAr['temperature']['temp_min']))

    return "Today is going to be a wicked day with the current temperature at {} degrees, humidity at {} percent and windspeed at {} meters per second.".format(currentTemp, humidity, windSpeed)

def getCurrentWeather(location):
    owm = pyowm.OWM(api.openWeatherMapApiKey)
    observation = owm.weather_at_place(location)
    w = observation.get_weather() # <Weather - reference time=2013-12-18 09:20,
                                  # status=Clouds>

    weatherObject = {}

    weatherObject['wind']        = w.get_wind()
    weatherObject['humidity']    = w.get_humidity()
    weatherObject['temperature'] = w.get_temperature('celsius')
    weatherObject['status']      = w.get_temperature('celsius')

    return weatherObject

if __name__ == "__main__":
    init()

# Will it be sunny tomorrow at this time in Milan (Italy) ?
# forecast = owm.daily_forecast("Milan,it")
# tomorrow = pyowm.timeutils.tomorrow()
# forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Weather details
#w.get_wind()                  # {'speed': 4.6, 'deg': 330}
#w.get_humidity()              # 87
#w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)
