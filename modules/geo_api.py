import requests
from decouple import config
class GeoAPI:
    API_KEY = config('API_KEY')
    LAT = config('LAT')
    LON = config('LON')
    @classmethod
    def is_hot_in_pehuajo(cls, api_key=API_KEY, lat=LAT, lon=LON, temp=28):
        
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        try:
            r = requests.get(url).json()
        except:
            return False
        #Get Temperature from request
        location_temp=r.get('main').get('temp')
        if (location_temp)>temp:
            return True
        else:
            return False

