import requests

def findTemperatureLive():  
    """Print the current temperature in Boston using data from boston.com.
  
    This function depends on knowledge of the page structure - if they change
    the page structure, the program will not work!  The page structure changed
    during Summer 2021.  The code below works as of 2021-08-26.
    """

    # Get the weather page
    weather = requests.get("https://www.boston.com/weather").text
    # The temperature can be found after the span class label
    # "local-weather__current-info-temp" and immediately before the
    # HTML code "<sup>&deg</sup>; (the superscript degree symbol)
    curLoc = weather.find("local-weather__current-info-temp")
    strr = ''
    if curLoc != -1:
        # Now, find the degree symbol ("<sup>&deg;") following the temperature
        degLoc = weather.find("<sup>&deg", curLoc)
        # The temperature number is preceded by an HTML tag
        tempLoc = weather.rfind(">", 0, degLoc)
        # Temperature value is everything between the tag and the degree symbol
        strr = f"Temperature in Boston is {weather[tempLoc+1:degLoc]}, degrees"
        return strr
    else: 
        strr = "Page format has changed; cannot find the temperature"
        return strr
def findLoc(zip):
    ''' uses Zippotam to get the lat, lon, and name of city, and uses open meteo to get weather
    
    '''
    data = requests.get(f'https://api.zippopotam.us/us/{zip}?').json()
    place = data['places'][0]['place name']
    lat = data["places"][0]["latitude"]
    lon = data["places"][0]["longitude"]

    tempjson = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true").json()
    temp = tempjson["current_weather"]["temperature"]
    tempstring = f"Current Temperature: {temp}°C {(temp * 1.8) + 32}°F"
    return (place,tempstring)
    
if __name__ == "__main__":
    print(findTemperatureLive())
    findLoc('01984')