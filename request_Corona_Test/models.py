from django.db import models
from django.utils import timezone


class RequestCoronaTest(models.Model):
    # testRequestID = models.CharField(max_length=120, blank=True, default='')
    # def save(self, force_insert=False, force_update=False):
    #     if self.testRequestID == "":
    #         existing_testRequestIDs = RequestCoronaTest.objects.all().order_by('-testRequestID')
    #         if existing_testRequestIDs.count() > 0:
    #             new_testRequestID = int(existing_testRequestIDs[0].code[1:]) + 1
    #         else:
    #             new_testRequestID = 0
    #         self.testRequestID = 'T%03d' % new_testRequestID
    #     super(RequestCoronaTest, self).save(force_insert, force_update)

    name = models.CharField(max_length=120, default='')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField(default=timezone.now)
    preparedDateOfTest = models.DateField(default=timezone.now)
    time = models.CharField(max_length=120, default='')
    address = models.CharField(max_length=120, default='')
    preferedStateOfTest = models.CharField(max_length=120, default='')
    dob = models.CharField(max_length=120, default='')
    sex = models.CharField(max_length=50,blank=True, default='')
    # state = models.CharField(max_length=50, blank=True, default='')
    # lga = models.CharField(max_length=50, blank=True, default='')
    # ward = models.CharField(max_length=50, blank=True, default='')
    state = models.CharField(max_length=120, default='')
    lga = models.CharField(max_length=120, default='')
    ward = models.CharField(max_length=120, default='')
    polling_unit = models.CharField(max_length=120, default='')
    note = models.CharField(max_length=120, default='')

    def __str__(self):
        return self.name

class Material(models.Model):
    title = models.CharField(max_length=120, default='')
    description = models.CharField(max_length=20, default='')
    author = models.CharField(max_length=120, default='')
    date = models.DateField(default=timezone.now)
    material = models.URLField(max_length=2000, unique=False, blank=True, default='')

    def __str__(self):
        return f"{self.title}-{self.material.description}"





