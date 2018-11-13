#!/usr/bin/env python3

#imports
import argparse
import json
import requests
import sys

#"constants"
APIXU_BASE_URL = 'https://api.apixu.com/v1/forecast.json?key='
APIXU_FILE_NAME = 'apixukey.txt'

#script arguments parser
parser = argparse.ArgumentParser(description='Why look out of the window when you can get the weather info right in the terminal?')
parser.add_argument('-l', '--location', default="Poznan", help="set city name")
parser.add_argument('-e', help="get extra advice", action="store_true")
parser.add_argument('-k', '--key', help="set apixu key")
args = parser.parse_args()

def form_url(key, location):
    return(APIXU_BASE_URL + key + '&q=' + location)

def get_data(key, location):
    j = requests.get(form_url(key, location))
    return(json.loads(j.text))

def give_advice(temperature_celsius):
    if temperature_celsius < 10:
        return("Too cold, don't go outside.")
    elif temperature_celsius > 25:
        return("Too hot, don't go outside.")
    else:
        return("It's fine outside, but do you really want to leave your computer home alone? :(")

def save_key_to_file(key, filename):
    with open(filename, 'w') as file:
        file.write(key)
        file.close()

def read_key_from_file(filename):
    try:
        with open(APIXU_FILE_NAME) as file: key = file.read()
    except FileNotFoundError:
        print("Apixu key not found. Try rerunning the script with -k <your apixu key>.")
        sys.exit(1)
    return(key)

def get_weather_info(data_list, arg, *args):
    d = data_list.get(arg)
    for a in args:
        try:
            d = d.get(a)
        except AttributeError:
            d = d[0]
            d = d.get(a)
    return(d) 

### run

if args.key:
    save_key_to_file(args.key, APIXU_FILE_NAME)
    key = args.key
else:
    key = read_key_from_file(APIXU_FILE_NAME)

data_list = get_data(key, args.location)

location = get_weather_info(data_list, 'location', 'name')
location_country = get_weather_info(data_list, 'location', 'country')
temperature_celsius = get_weather_info(data_list, 'current', 'temp_c')
feelslike_celsius = get_weather_info(data_list, 'current', 'feelslike_c')
weather_condition = get_weather_info(data_list, 'current', 'condition', 'text')
windspeed = get_weather_info(data_list, 'current', 'wind_kph')
sunrise = get_weather_info(data_list, 'forecast', 'forecastday', 'astro', 'sunrise')
sunset = get_weather_info(data_list, 'forecast', 'forecastday', 'astro', 'sunset')

print("Location: {location} in {location_country}, weather condition: {weather_condition}".format(location=location, location_country=location_country, weather_condition=weather_condition)) 
print("Temperature: {temperature}C, feels like: {feelslike_temperature}C.".format(temperature=temperature_celsius, feelslike_temperature=feelslike_celsius))
print("Wind speed: {windspeed} kmph.".format(windspeed=windspeed))
print("The sun rises at {sunrise} and sets at {sunset}".format(sunrise=sunrise, sunset=sunset))

if args.e:
    give_advice(temperature_celsius)
