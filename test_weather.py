#imports
import unittest
import requests
from weather import form_url, save_key_to_file, get_data
from nose.tools import assert_is_not_none 

class WeatherTestCase(unittest.TestCase):
    """Tests for weather.py"""

    APIKEY = "somekey"
    APICALL_URL = "https://apicallurl.domain/something/more"

    def test_url_formation(self):
        self.assertEqual(form_url(APIKEY, "Poznan"), APICALL_URL) 

    def test_save_key_to_file(self):
        save_key_to_file("magic_key", "file.txt")
        with open('file.txt') as file: key = file.read()
        self.assertEqual("magic_key", key)

    def test_request_response(self):
        response = get_data(APIKEY, "Poznan")
        assert_is_not_none(response)

if __name__ == '__main__':
    unittest.main()
