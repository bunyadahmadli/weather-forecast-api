
import  requests
import json


url = 'https://eu1.locationiq.com/v1/search.php'

def get_lat_lon(location):
    
    response = requests.get(url,params={"key":"a1779b7817b3b2","q":location,"format":"json"})
    
    if response.status_code==200:
        result = response.json()
        
        lat = result[0]["lat"]
        lon = result[0]["lon"]
        
        return lat,lon
    
            
    

def max_and_min_temp_byday(today_temps):
    today_max_temp = today_temps['hourly']['data'][0]['apparentTemperature']
    today_min_temp = today_temps['hourly']['data'][0]['apparentTemperature']

    for x in today_temps['hourly']['data']:
        if (x['apparentTemperature'] < today_min_temp):
            today_min_temp = x['apparentTemperature'] 
            
        if (x['apparentTemperature'] > today_max_temp):
            today_max_temp = x['apparentTemperature'] 
            
    return today_max_temp,today_min_temp

def max_and_min_temp_byweek(week_temps):
    week_max_temp = week_temps['daily']['data'][0]['apparentTemperatureLow']
    week_min_temp = week_temps['daily']['data'][0]['apparentTemperatureMax']

    for x in week_temps['daily']['data']:
        if (x['apparentTemperatureLow'] < week_min_temp):
            week_min_temp = x['apparentTemperatureLow'] 
        
        if (x['apparentTemperatureMax'] > week_max_temp):
            week_max_temp = x['apparentTemperatureMax'] 
    
    return week_max_temp,week_min_temp
            

    
    
#url = https://api.darksky.net/forecast/[key]/[latitude],[longitude]
def get_wheather_forecast(location):
    
    lat,lon = get_lat_lon(location)

    url = 'https://api.darksky.net/forecast/f3146e0fc78b4930d41a60703c08e2ae/{},{}'.format(lat,lon)
    
    response = requests.get(url)
    if response.status_code==200:
        result = response.json()
        data = {}
        data["apparent_temp"] = result["currently"]["apparentTemperature"]
        
        data["today_max_temp"], data["today_min_temp"] = max_and_min_temp_byday(result)
        data["week_max_temp"], data["week_min_temp"]  = max_and_min_temp_byweek(result)

        return data
            
        
    

            