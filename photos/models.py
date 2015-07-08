from django.db import models
from django.contrib.auth.models import User

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENSES=(
    (COPYRIGHT,'copytright'),
    (COPYLEFT,'copyleft'),
    (CREATIVE_COMMONS,'Creative Commons')
)

PUBLIC = 'PUB'
PRIVATE = 'PRI'

VISIBILITY=(
    (PUBLIC,'Publica'),
    (PRIVATE,'Privada')
)
# Create your models here.
class Photo(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    url=models.URLField()
    description = models.TextField(blank=True,null=True,default="")
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3,choices=LICENSES)
    visibility = models.CharField(max_length=3, choices= VISIBILITY, default=PUBLIC)


    def __unicode__(self):
        return self.name