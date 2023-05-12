from django.contrib import admin

import inspect
from app import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.StationLocation)
admin.site.register(models.Weather)
admin.site.register(models.WeatherPredictModel)
admin.site.register(models.EmailHistory)