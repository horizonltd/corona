from django.db import models
from django.utils import timezone


class RequestCoronaTest(models.Model):
    time_choices = (
        ('morning', "Morning"),
        ('evening', "Evening")
    )
    state_choices = (
        ('kaduna', "Kaduna"),
        ('lagos', "Lagos"),
        ('abuja', "Abuja"),
        ('oyo', "Oyo"),
        ('ogun', "Ogun"),
        ('bauchi', "Bauchi"),
        ('enugu', "Enugu"),
        ('edo', "Edo"),
        ('osun', "Osun"),
        ('benue', "Benue"),
        ('ekiti', "Ekiti"),
    )
    testRequestID = models.CharField(max_length=120, blank=True, default='')
    def save(self, force_insert=False, force_update=False):
        if self.testRequestID == "":
            existing_testRequestIDs = RequestCoronaTest.objects.all().order_by('-testRequestID')
            if existing_testRequestIDs.count() > 0:
                new_testRequestID = int(existing_testRequestIDs[0].code[1:]) + 1
            else:
                new_testRequestID = 0
            self.testRequestID = 'T%03d' % new_testRequestID
        super(RequestCoronaTest, self).save(force_insert, force_update)

    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField(default=timezone.now)
    preparedDateOfTest = models.DateField(default=timezone.now)
    time = models.CharField(choices=time_choices, max_length=10)
    address = models.CharField(max_length=120, default='')
    preferedStateOfTest = models.CharField(choices=state_choices,max_length=120, default='')
    dob = models.DateField(default=timezone.now)
    sex = models.CharField(max_length=50,blank=True, default='')
    # state = models.CharField(max_length=50, blank=True, default='')
    # lga = models.CharField(max_length=50, blank=True, default='')
    # ward = models.CharField(max_length=50, blank=True, default='')
    state = models.ForeignKey(to='State', related_name='volunteers', on_delete=models.CASCADE)
    lga = models.ForeignKey(to='Lga', related_name='volunteers', on_delete=models.CASCADE)
    ward = models.ForeignKey(to='Ward', related_name='volunteers', on_delete=models.CASCADE)
    polling_unit = models.CharField(max_length=50, blank=True, default='')
    note = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

class Lga(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

class Ward(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

class Specialization(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name




class Material(models.Model):
    title = models.CharField(max_length=120, default='')
    description = models.CharField(max_length=20, default='')
    author = models.CharField(max_length=120, default='')
    date = models.DateField(default=timezone.now)
    material = models.FileField(upload_to='material/', blank=True, null=True, default='')

    def __str__(self):
        return f"{self.title}-{self.material.description}"





