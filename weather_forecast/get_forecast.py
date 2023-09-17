import click
import requests
from weather_forecast.constants import *


def get_forecast(city, days):
    data = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                     params={'q': city, 'type': WEATHER_TYPE, 'units': UNITS, 'lang': LANG, 'APPID': APPID}).json()
    weather_data = data['list']

    days_count = 0
    prev_day = ""

    for data in weather_data:
        curr_day = str(data['dt_txt']).split(" ")[0]

        if curr_day != prev_day:
            days_count += 1
            prev_day = curr_day

        if days_count <= days:
            click.echo(data['dt_txt'] + " " + '{0:+3.0f}'.format(data['main']['temp']) + " " + data['weather'][0]['description'])
        else:
            return
