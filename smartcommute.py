from collections import OrderedDict
import requests
    
def printTripDuration(duration):
    """prints the time (in min) to get from start to end"""
    print("If you leave now, it will take you " +
          duration + " to get from " + start + " to " + end)
    
    
def googleQueryLink(key, a, b):
    """Generates a google map api query link to get from
       location a to b. Must be provided a key"""
    base = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    aMod, bMod = a, b
    #TODO: deal with repeating invalid chars (ie MD, 25431 ==> MD++25431)
    for ch in [' ', '.', ',', '\'']:
        if ch in aMod:
            aMod = aMod.replace(ch,'+')
        if ch in bMod:
            bMod = bMod.replace(ch,'+')
    params = ('origins=' + aMod + '&destinations=' + bMod +
              '&traffic_model=best_guess&departure_time=now&units=imperial' +
              '&key=' + key)
    return base + params
    
    
def weatherQueryLink(key,zipCode):
    """Generates a Open Weather Map query link
       Must be provided a key"""
    base = 'http://api.openweathermap.org/data/2.5/weather?'
    params = 'zip=' + str(zipCode) + ',us&units=imperial&appid=' + key
    return base + params
    
def displayCommute(data):
    """Prints today's Smart Commute info"""
    print("Hello, here is your Smart Commute summary for today:")
    print('*****************************')
    for k, v in data.items():
        print(k,':', v)
    print('*****************************')    
    
if __name__ == '__main__':
    
    googleKey = '<Obtain Free API Key from developers.google.com>'
    openWeatherMapKey = '<Obtain free API Key from openweathermap.org>'
    
    start = 'New York City' #substitute with your starting address
    end = 'Disney Land Florida' #substitute with your destination
    zipCode = 11111 #substitute with zipcode for weather data
    
    data = OrderedDict()
    
    queryGoogleUrl = googleQueryLink(googleKey, start, end)
    r = requests.get(queryGoogleUrl)
    trip = r.json()
    tripElements = trip['rows'][0]['elements'][0]
    data['distance'] = tripElements['distance']['text']
    data['duration'] = tripElements['duration']['text']
    data['trafficDuration'] = tripElements['duration_in_traffic']['text']
    
    queryWeatherUrl = weatherQueryLink(openWeatherMapKey, zipCode)
    r = requests.get(queryWeatherUrl)
    weather = r.json()
    data['hi'] = weather['main']['temp_max']
    data['low'] = weather['main']['temp_min']
    data['wind'] = weather['wind']['speed']
    data['description'] = weather['weather'][0]['description']
    
    displayCommute(data)
    
    print("Script over...\nPress Enter to exit.")
    input()
