import click
import requests
from weather_forecast.constants import *


def check_days(days):
    if not (isinstance(days, int)) or (days < 1) or (days > 5):
        click.echo("The number of days must be integer between 1 and 5.")
        return False
    return True


def check_city(city):
    if city is None:
        click.echo("City is a required argument.")
        return False

    try:
        data = (requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': city, 'type': WEATHER_TYPE, 'units': UNITS, 'APPID': APPID})
                .json())

        if len(data['list']) > 0:
            return True
        else:
            click.echo("The city you provided is not found.")
            return False

    except Exception as e:
        print("Exception while searching for the city:", e)
        pass
