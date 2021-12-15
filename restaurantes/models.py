from django.db import models

# Create your models here.
class Restaurants(models.Model):
    id = models.TextField(primary_key=True)
    rating = models.IntegerField(null=True)
    name = models.CharField(max_length=150,null=True)
    site = models.CharField(max_length=150, unique = True,null=True)
    email = models.EmailField('Correo electronico', max_length=150,null=True)
    phone = models.CharField(max_length=30,null=True)
    street = models.TextField(null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    
    def __str__(self) -> str:
        return self.name