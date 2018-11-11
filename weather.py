#!/usr/bin/env python3

#imports
import argparse
import json
import sys
from urllib.request import urlopen

APIXU_BASE_URL = 'https://api.apixu.com/v1/current.json?key='
APIXU_FILE_NAME = 'apixukey.txt'

def parse_args():
    parser = argparse.ArgumentParser(description='Why look out of the window when you can get the weather info right in the terminal?')
    parser.add_argument('-l', '--location', default="Poznan", help="set city name")
    parser.add_argument('-e', help="get extra advice", action="store_true")
    parser.add_argument('-k', '--key', help="set apixu key")
    return parser.parse_args()

def form_url(key, location):
    return APIXU_BASE_URL + key + '&q=' + location

def get_data(url):
    j = urlopen(url) 
    return json.load(j)

def give_advice():
    pass

def save_key_to_file(key, filename):
    with open(filename, 'w') as file:
        file.write(key)
        file.close()

args = parse_args()
print(args)

if args.key:
   save_key_to_file(args.key, APIXU_FILE_NAME)
else:
    try:
        with open(APIXU_FILE_NAME) as file: key = file.read()
    except FileNotFoundError:
        print("Apixu key not found. Try rerunning the script with -k <your apixu key>.")
        sys.exit(1)



