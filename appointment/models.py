from django.db import models
from hospital.models import Doctor
from django.utils import timezone


class Appointment(models.Model):
    time_choices = (
        ('morning', "Morning"),
        ('evening', "Evening")
    )
    state_choices = (
        ('kaduna', "Kaduna"),
        ('lagos', "Lagos"),
         ('abuja', "Abuja")
    )

    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    doctor = models.ForeignKey(
     Doctor, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
    date = models.DateField(default=timezone.now)
    preparedDateOfTest = models.DateField(default=timezone.now)
    time = models.CharField(choices=time_choices, max_length=10)
    address = models.CharField(max_length=120, default='')
    preferedStateOfTest = models.CharField(choices=state_choices,max_length=120, default='')
    dob = models.DateField(default=timezone.now)
    code = models.CharField(max_length=2000, blank=True)


    
    sex = models.CharField(max_length=50,blank=True, default='')
    state = models.CharField(max_length=50, blank=True, default='')
    lga = models.CharField(max_length=50, blank=True, default='')
    ward = models.CharField(max_length=50, blank=True, default='')
    polling_unit = models.CharField(max_length=50, blank=True, default='')

    note = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return f"{self.name}-{self.doctor.name}"

class Material(models.Model):
    title = models.CharField(max_length=120, default='')
    description = models.CharField(max_length=20, default='')
    author = models.CharField(max_length=120, default='')
    date = models.DateField(default=timezone.now)
    material = models.FileField(upload_to='material/', blank=True, null=True, default='')

    def __str__(self):
        return f"{self.title}-{self.material.description}"








# from django.db import models
# from hospital.models import Doctor
# from django.utils import timezone


# class Reqeuest_Corona_Test(models.Model):
#     time_choices = (
#         ('morning', "Morning"),
#         ('evening', "Evening")
#     )
#     state_choices = (
#         ('kaduna', "Kaduna"),
#         ('lagos', "Lagos"),
#          ('abuja', "Abuja")
#     )

#     name = models.CharField(max_length=120)
#     phone = models.CharField(max_length=20)
#     email = models.EmailField()
#     doctor = models.ForeignKey(
#      Doctor, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
#     date = models.DateField(default=timezone.now)
#     preparedDateOfTest = models.DateField(default=timezone.now)
#     time = models.CharField(choices=time_choices, max_length=10)
#     address = models.CharField(max_length=120, default='')
#     preferedStateOfTest = models.CharField(choices=state_choices,max_length=120, default='')
#     dob = models.DateField(default=timezone.now)
#     code = models.CharField(max_length=2000, blank=True)


    
#     sex = models.CharField(max_length=50,blank=True, default='')
#     state = models.CharField(max_length=50, blank=True, default='')
#     lga = models.CharField(max_length=50, blank=True, default='')
#     ward = models.CharField(max_length=50, blank=True, default='')
#     polling_unit = models.CharField(max_length=50, blank=True, default='')

#     note = models.TextField(blank=True, null=True, default='')

#     def __str__(self):
#         return f"{self.name}-{self.doctor.name}"
