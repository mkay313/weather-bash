#!/usr/bin/env python3

#imports
import argparse
import json
import sys
from urllib.request import urlopen
import urllib.error

APIXU_BASE_URL = 'https://api.apixu.com/v1/forecast.json?key='
APIXU_FILE_NAME = 'apixukey.txt'

def parse_args():
    parser = argparse.ArgumentParser(description='Why look out of the window when you can get the weather info right in the terminal?')
    parser.add_argument('-l', '--location', default="Poznan", help="set city name")
    parser.add_argument('-e', help="get extra advice", action="store_true")
    parser.add_argument('-k', '--key', help="set apixu key")
    return parser.parse_args()

def form_url(key, location):
    return APIXU_BASE_URL + key + '&q=' + location

def get_data(key, location):
    try:
        j = urlopen(form_url(key, location))
    except urllib.error.HTTPError:
        print("Invalid request. Perhaps your key or location is invalid?")
        sys.exit(1)
    return json.load(j)

def give_advice(temperature_celsius):
    if temperature_celsius < 10:
        print("Too cold, don't go outside.")
    elif temperature_celsius > 25:
        print("Too hot, don't go outside.")
    else:
        print("It's fine outside, but do you really want to leave your computer home alone? :(")

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
    return key

args = parse_args()

if args.key:
   save_key_to_file(args.key, APIXU_FILE_NAME)
   key = args.key
else:
   key = read_key_from_file(APIXU_FILE_NAME)
   
json_data = get_data(key, args.location)
print("The current temperature is {} degrees Celsius.".format(int(json_data["current"]["temp_c"])))
give_advice(int(json_data["current"]["temp_c"]))
