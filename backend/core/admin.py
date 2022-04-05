from django.contrib import admin
from django.contrib.gis import admin as geoadmin

from leaflet.admin import LeafletGeoAdmin
from .models import *
# Register your models here.

class locationAdmin( LeafletGeoAdmin):
  
    settings_overrides =  {
        'DEFAULT_CENTER': (28.333, 84.000),
        'DEFAULT_ZOOM': 8,
        'MIN_ZOOM': 5,  
        'MAX_ZOOM': 24,
        'TILES': [('Google Terrain','http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}',''),('OSM','https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',''),('Google Satellite','http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}','')],
    }
 
    list_display = ('latlng',)
  

admin.site.register(location,locationAdmin)
@admin.register(Dataset)
class DatasetAdmin(geoadmin.GeoModelAdmin):
    list_display = [
        'name', "created_by" ]
@admin.register(Element)
class DatasetAdmin(admin.ModelAdmin):
    list_display = [
         "dataset_id","created_by" ]

