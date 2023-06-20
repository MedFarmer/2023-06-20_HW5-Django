from django.db import models

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50)
    hotel_address = models.CharField(max_length=100)
    hotel_description = models.CharField(max_length=500)

    def __str__(self):
        return self.hotel_name
