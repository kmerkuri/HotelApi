from django.db import models

# Create your models here.


class FindHotels(models.Model):
    user=models.CharField(max_length=50),
    hotels=models.CharField(max_length=50)
    def __str__(self):
        return self.hotels
    

    