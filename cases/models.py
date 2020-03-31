from django.db import models


class TestCenter(models.Model):
    name = models.CharField(max_length=120, default='')
    address = models.CharField(max_length=120, default='')
    picture = models.ImageField(upload_to="center/", default='')
    latitude = models.CharField(max_length=120,blank=True, null=True, default='')
    longitude = models.CharField(max_length=120,blank=True, null=True, default='')
    details = models.TextField(blank=True, null=True, default='')



    def __str__(self):
        return self.name

class Country(models.Model):
    country = models.CharField(max_length=100, default='')
    date = models.DateField(default=2019-12-13)
    confirmed = models.CharField(max_length=100, default='')
    death = models.CharField(max_length=100, default='')
    recovered = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.country

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='state')
    state = models.CharField(max_length=100, default='')
    date = models.DateField(default=2019-12-13)
    confirmed = models.CharField(max_length=100, default='')
    death = models.CharField(max_length=100, default='')
    recovered = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.state










