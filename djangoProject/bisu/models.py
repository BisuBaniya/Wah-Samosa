from django.db import models
from django.utils import timezone

# Create your models here.

class SamosaVariety(models.Model):
    SAMOSA_TYPE_CHOICE = [
        ('PN','Paneer'),
        ('AL','Aloo'),
        ('PJ','Punjabi'),
        ('PS','Pasta'),
        ('CM','Chowmein'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='bisu/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=SAMOSA_TYPE_CHOICE)
    