# weather_forecast
Command line tool that provides you from 1 to 5 day weather forecast.

## To use this package you will need:

1. In your terminal execute
```bash
pip install git+ssh://git@github.com/merirut/weather_forecast.git
```
2. Now you can run it! For example,
```bash
weather_forecast --city "Saint Petersburg,RU" --days 2
```
Output will look like \
<sub>
2023-09-17 12:00:00 +18 clear sky \
2023-09-17 15:00:00 +16 light rain \
2023-09-17 18:00:00 +13 scattered clouds \
</sub> \
And so on...

## Options:

```--city``` The city for which you want to know the weather forecast. Required. \
```--days``` Number of days you want to see in the weather forecast (from 1 to 5). Default = 1. \
```--help``` Prints help.