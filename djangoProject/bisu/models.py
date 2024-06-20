from django.db import models # type: ignore
from django.utils import timezone # type: ignore
from django.contrib.auth.models import User #type: ignore

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
    description = models.TextField(default='')
    price = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
#One to many
    
class SamosaReview(models.Model):
    samosa = models.ForeignKey(SamosaVariety,on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
#Many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    samosa_varieties = models.ManyToManyField(SamosaVariety,related_name='stores')

    def __str__(self):
        return self.name

#One to one

class SamosaCertificate(models.Model):
    samosa = models.OneToOneField(SamosaVariety, on_delete=models.CASCADE, related_name='certificate')    
    certificate_number = models.CharField(max_length=100)
    issued_added = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.name.samosa}'
    
    
    

