from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings



class TypeOfMembership(models.Model):
    membership_type = models.CharField(max_length=150)
    #member_entry = models.CharField(max_length=150)

    def __str__(self):
        return self.membership_type

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=20, unique=True)
    phone_number = models.CharField(blank=True, null=True, max_length=14, unique=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name','email']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    payment_status = models.CharField(max_length=100)
    balance = models.CharField(max_length=100)
    membership_type = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='uploads', blank=True)



