

#imports
import unittest
from weather import form_url

APIXU_BASE_URL = 'https://api.apixu.com/v1/current.json?key='

class WeatherTestCase(unittest.TestCase):
    """Tests for `weather.py`."""

    def test_url_formation(self):
        self.assertEqual(form_url("2f0115073b344ca7be6194156171611", "Poznan"), "https://api.apixu.com/v1/current.json?key=2f0115073b344ca7be6194156171611&q=Poznan") 

if __name__ == '__main__':
    unittest.main()
