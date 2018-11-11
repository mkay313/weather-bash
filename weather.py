#!/usr/bin/env python3

#imports
import argparse
import json
from urllib.request import urlopen

APIXU_BASE_URL = 'https://api.apixu.com/v1/current.json?key=' 

def parse_args():
    parser = argparse.ArgumentParser(description='Why look out of the window when you can get the weather info right in the terminal?')
    parser.add_argument('-l', '--location', default="Poznan", help="set city name")
    parser.add_argument('-e', help="get extra advice", action="store_true")
    return parser.parse_args()

def form_url(key, location):
    return APIXU_BASE_URL + key + '&q=' + location

def get_data(url):
    j = urlopen(url) 
    return json.load(j)

def give_advice():
    pass

args = parse_args()
print(args)
print(get_data(form_url("2f0115073b344ca7be6194156171611", "Poznan")))
