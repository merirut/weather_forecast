import click
from weather_forecast.check_args import check_days, check_city
from weather_forecast.get_forecast import get_forecast


@click.command()
@click.option("--city", help="The city you want to ")
@click.option("--days", default=1, help="Number of days you want to see in the forecast (from 1 to 5).")
def run(city, days):
    if not check_days(days) or not check_city(city):
        print_help_and_exit()
    else:
        get_forecast(city, days)


def print_help_and_exit():
    ctx = click.get_current_context()
    click.echo(ctx.get_help())
    ctx.exit()
