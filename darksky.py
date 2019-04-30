import forecastio
from Latitude_Longitude import get_lat_long

api = "2ba768c7df97241b0c0ee394a23b880d"


def get_temperature(address):
        lat = get_lat_long(address)['lat']
        long = get_lat_long(address)['lng']
        forecast = forecastio.load_forecast(api, lat, long, units='us')
        return forecast.currently().time


def get_weather(address):
        lat = get_lat_long(address)['lat']
        long = get_lat_long(address)['lng']
        forecast = forecastio.load_forecast(api, lat, long)
        return forecast.currently().icon










