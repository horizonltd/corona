from django.db import models



class Timeline(models.Model):
    first_Name = models.CharField(max_length=120)
    middle_Name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    sex = models.CharField(max_length=120)
    state = models.CharField(max_length=120, default='')
    lga = models.CharField(max_length=120, default='')
    ward = models.CharField(max_length=120, default='')
    polling_Unit = models.CharField(max_length=120)
    geolocation = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone_Number = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True, default='')
    reportDate = models.CharField(max_length=120)

    def __str__(self):
        return self.first_Name


