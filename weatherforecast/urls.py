from django.urls import path
from .views import WeatherAPIView


app_name ='weatherforecast'
urlpatterns = [
    path('weather/<str:location>/', WeatherAPIView.as_view(), name='weather'),
]

