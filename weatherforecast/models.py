from django.db import models

# Create your models here.

class WeatherForecast(models.Model):
    location = models.CharField(max_length=100)
    apparent_temperature = models.FloatField(null=True, blank=True)
    lowest_temperature_today = models.FloatField(null=True, blank=True)
    highest_temperature_today =  models.FloatField(null=True, blank=True)
    lowest_temperature_next_week =  models.FloatField(null=True, blank=True)
    highest_temperature_next_week =  models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.location