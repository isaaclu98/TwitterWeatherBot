import requests


def valid_address(address):
    response = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=AIzaSyCdKMTNhBcKsb2gmzXORwF7XIbJe53fTcY')
    resp_json_payload = response.json()
    return resp_json_payload['status']


def get_lat_long(address):
    response = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json?address=' + address +'&key=AIzaSyCdKMTNhBcKsb2gmzXORwF7XIbJe53fTcY')
    resp_json_payload = response.json()
    return resp_json_payload['results'][0]['geometry']['location']


