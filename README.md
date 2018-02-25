# weather-bash

###How to run
Run from the cloned repository with ./weather.sh or copy the file into your /home/bin to run it from anywhere

###About
Why look out of the window when you can check the weather on your computer without leaving the console?
This is a slightly modified version of a fun homework assignment for my studies at AMU Poznan.
It uses the [apixu.com weather api](https://www.apixu.com) and [sunrise-sunset api](https://api.sunrise-sunset.org) to fetch data; add your apixu.com key with the -k flag when running the script for the first time.
The default location is set to Poznan. Run the script with -l [ARG] to set your own location (it is not kept permanently).
Run the script with -k [ARG] to add your apixu.com key to a temp file.
Run the script with -e for extra weather advice.
Run the script with -f to get the weather forecast for tomorrow.