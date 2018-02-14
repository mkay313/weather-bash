#TODO: add option to support different timezones (only supports UTC time atm)
#TODO: add forecasting
#TODO: add option to get the APIXU key from the console/file

#!/bin/bash

#checks if jq is installed 
command -v jq >/dev/null 2>&1 || { echo >&2 "jq needs to be installed for this script to work. Try: sudo apt-get install jq"; }

#change the APIXUKEY sequence to your own key
apikey=http://api.apixu.com/v1/current.json?key=2f0115073b344ca7be6194156171611\&q=

#passing the options
while getopts l:eh option
do
    case "${option}"
    in
    l) locationname=${OPTARG};;
    e) easteregg="true";;
    h) printf "Why look out of the window when you can check the weather on your computer without leaving the console?\n"
       printf "Default location: Poznan. Run the script with -l [ARG] to set your own location.\n"
       printf "Run the script with -e for extra weather advice.\n"
       exit
    esac
done

#default location = Poznan
    if [ -z ${locationname+x} ]; then 
        locationname=Poznan
    fi
    currentlocation=$(echo $locationname)

#putting the key & location together
    myapikey=$apikey$locationname

#get the weather data
    curl --silent $myapikey | jq '.' | cat > /tmp/weathertmp
   
    cityname=$(cat /tmp/weathertmp | jq '.location | .name' | tr -d '""')
    conditions=$(cat /tmp/weathertmp | jq '.current | .condition | .text' | tr -d '""')
    localtime=$(cat /tmp/weathertmp | jq '.location | .localtime' | tr -d '""')
    temp=$(cat /tmp/weathertmp | jq '.current | .temp_c')
    feelslike=$(cat /tmp/weathertmp | jq '.current | .feelslike_c')
    windspeed=$(cat /tmp/weathertmp | jq '.current | .wind_kph')

#get the longitute and latitude data for the city
    lat=$(cat /tmp/weathertmp | jq '.location | .lat')
    long=$(cat /tmp/weathertmp | jq '.location | .lon')

#get the sunrise/sunset/day length data
    curl --silent https://api.sunrise-sunset.org/json?lat=$lat\&lng=$long | jq '.' | cat > /tmp/daytemp
    
    sunrise=$(cat /tmp/daytemp | jq '. | .results | .sunrise' | tr -d '""')
    sunset=$(cat /tmp/daytemp | jq '. | .results | .sunset' | tr -d '""')
    daylength=$(cat /tmp/daytemp | jq '. | .results | .day_length' | tr -d '""')

#print
    printf "W E A T H E R  F O R E C A S T\n"
    printf "Location: %s  Conditions: %s\n" "$cityname" "$conditions"
    printf "Time: %s\n" "$localtime"
    printf "The sun rises at %s and sets at %s UTC\n" "$sunrise" "$sunset"
    printf "The day is %s long\n" "$daylength"
    printf "Temperature: %sC, feels like: %sC\n" "$temp" "$feelslike"
    printf "Wind speed: %s kmph\n" "$windspeed"

#easteregg
    if [[ $easteregg = "true" ]]; then
        temp_formatted=$(echo ${temp%.*}) #this is magic: you don't want the temp to be a float in bash
        if [[ temp_formatted -lt 10 ]]; then printf "Too cold, don't go outside.\n"
        elif [[ temp_formatted -gt 25 ]]; then printf "Too hot, don't go outside.\n"
        else printf "It's fine outside, but do you r e a l l y want to leave your computer home alone? :(\n"
        fi
    fi
