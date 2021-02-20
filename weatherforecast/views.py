import json
from django.shortcuts import render
from django.core.cache import cache
from datetime import  datetime,date
from rest_framework.generics import GenericAPIView
from .serializers import WeatherForecastSerializer
from .models import WeatherForecast
from rest_framework.response import Response
from rest_framework.permissions  import  IsAuthenticated
from .utils import get_lat_lon,get_wheather_forecast



class WeatherAPIView(GenericAPIView):
    serializer_class = WeatherForecastSerializer
    permission_classes = [IsAuthenticated,]

    def get(self,request, location, *args,**kwargs):
        weather = cache.get(location,version=3)
        
        if weather:
            data = json.loads(weather)
            
            return Response(weather)
       
        weather = WeatherForecast.objects.filter(location = location,created_at__date= date.today()).first()
        if weather:
            
            serializer = WeatherForecastSerializer(weather)
            data = json.dumps(serializer.data)
            
            cachce_key = cache.set(location,data,60*60)
            
            return Response(serializer.data)

        else:
            
            data = get_wheather_forecast(location)
            weather = WeatherForecast.objects.create(
                location = location,
                apparent_temperature = data["apparent_temp"],
                lowest_temperature_today=data["today_min_temp"],
                lowest_temperature_next_week= data["week_min_temp"],
                highest_temperature_today = data["today_max_temp"],
                highest_temperature_next_week =data["week_max_temp"]
            )
            serializer = WeatherForecastSerializer(weather)
            data = json.dumps(serializer.data)
            
            cachce_key = cache.set(location,data,60*60)
            
            
            return Response(serializer.data)

  

    


        















