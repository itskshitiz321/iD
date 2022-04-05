
from django.contrib.gis.db import models as geomodels
from django.db import models

# Create your models here.

class location (models.Model):
   # this is just a example model you can delete it later after project is setup , it is also tied up with the views for a API endpoint to get example of how endpoint will work 
    latlng = geomodels.PointField(null=True,unique=True)
   
    class Meta:
        verbose_name_plural = "location"

class Dataset (models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    name= models.CharField(max_length=255)
    created_by = models.IntegerField()
    last_modified= models.DateTimeField(auto_now=True)
    aoi = geomodels.MultiPolygonField(srid=4326)

def element_directory_path(instance, filename):
    """Plan is to create file path dynamically from models and tie it with the model itself , so that uploading row will do job for us

    Args:
        instance (_type_): _description_
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    # file will be uploaded to MEDIA_ROOT / trainings/
    # return 'trainings/{0}}_{1}_{2}_{3}'.format(instance.Element.id, filename)
    return None # None default for now should return filepath after creation
class Element (models.Model):
    # image_path= models.ImageField(upload_to=element_directory_path)
    image= models.ImageField(upload_to='data/') # added data for now but will be redirected to above funtion for dynamic name generation
    image_url= models.URLField(unique=True)
    image_get_date= models.DateTimeField(auto_now_add=True)
    dataset = models.ForeignKey(
        Dataset, to_field="id",on_delete=models.CASCADE)
    created_by = models.IntegerField()




  