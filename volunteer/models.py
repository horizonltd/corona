from django.db import models




class ReportCase(models.Model):
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





# class ReportCase(models.Model):
#     first_Name = models.CharField(max_length=120)
#     middle_Name = models.CharField(max_length=120)
#     surname = models.CharField(max_length=120)
#     sex = models.CharField(max_length=120)
#     state = models.ForeignKey(to='State', related_name='reportCases', on_delete=models.CASCADE)
#     lga = models.ForeignKey(to='Lga', related_name='reportCases', on_delete=models.CASCADE)
#     ward = models.ForeignKey(to='Ward', related_name='reportCases', on_delete=models.CASCADE)
#     polling_Unit = models.CharField(max_length=120)
#     geolocation = models.CharField(max_length=120)
#     email = models.EmailField(unique=True)
#     phone_Number = models.CharField(max_length=120)
#     description = models.TextField(blank=True, null=True, default='')
#     reportDate = models.DateField(max_length=120)

#     def __str__(self):
#         return self.first_Name



class Volunteer(models.Model):
    # preparedDaysTobeInvolved_choices = (
    #     ('monday', "Monday"),
    #     ('tuesday', "Tuesday"),
    #     ('sunday', "Sunday"),
    # )
    # state_choices = (
    #     ('kaduna', "Kaduna"),
    #     ('lagos', "Lagos"),
    #     ('abuja', "Abuja"),
    #     ('oyo', "Oyo"),
    #     ('ogun', "Ogun"),
    #     ('bauchi', "Bauchi"),
    #     ('enugu', "Enugu"),
    #     ('edo', "Edo"),
    #     ('osun', "Osun"),
    #     ('benue', "Benue"),
    #     ('ekiti', "Ekiti"),
    # )

    ##Auto Generated Field
    # entryID = models.CharField(max_length=120, blank=True, default='')
    # def save(self, force_insert=False, force_update=False):
    #     if self.entryID == "":
    #         existing_entryIDs = Volunteer.objects.all().order_by('-entryID')
    #         if existing_entryIDs.count() > 0:
    #             new_entryID = int(existing_entryIDs[0].code[1:]) + 1
    #         else:
    #             new_entryID = 0
    #         self.entryID = 'E%03d' % new_entryID
    #     super(Volunteer, self).save(force_insert, force_update)
    #Other part
    first_Name = models.CharField(max_length=120)
    middle_Name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    ##Relational
    qualification = models.CharField(max_length=120, default='')
    #Relational
    profession = models.CharField(max_length=120, default='')
    dob = models.DateField(max_length=120)
    sex = models.CharField(max_length=120)
    state = models.CharField(max_length=120, default='')
    lga = models.CharField(max_length=120, default='')
    ward = models.CharField(max_length=120, default='')
    polling_Unit = models.CharField(max_length=120)
    geolocation = models.CharField(max_length=120, default='')
    #choices
    prepared_State_of_To_Be_Involved = models.CharField(max_length=120, default='')
    prepared_Start_DateTobeInvolved = models.DateField(max_length=120)
    prepared_EndDate_To_be_Involved = models.DateField(max_length=120)
    #Choices
    prepared_Days_To_be_Involved = models.CharField(max_length=120, default='')
    # preparedStartTimeTobeInvolved = models.TimeField(blank=True)
    # preparedEndTimeTobeInvolved = models.TimeField(blank=True)
    email = models.EmailField(unique=True)
    phone_Number = models.CharField(max_length=120)
    date_Of_Entry = models.DateField(max_length=120)
    specialization = models.CharField(max_length=120, default='')
    picture = models.URLField(max_length=128, unique=True, blank=True, default='')

    def __str__(self):
        return self.first_Name




    # ##Auto Generated Field
    # entryID = models.CharField(max_length=120, blank=True, default='')
    # def save(self, force_insert=False, force_update=False):
    #     if self.entryID == "":
    #         existing_entryIDs = Volunteer.objects.all().order_by('-entryID')
    #         if existing_entryIDs.count() > 0:
    #             new_entryID = int(existing_entryIDs[0].code[1:]) + 1
    #         else:
    #             new_entryID = 0
    #         self.entryID = 'E%03d' % new_entryID
    #     super(Volunteer, self).save(force_insert, force_update)
    # #Other part
    # first_Name = models.CharField(max_length=120)
    # middle_Name = models.CharField(max_length=120)
    # surname = models.CharField(max_length=120)
    # ##Relational
    # qualification = models.ManyToManyField(to='Qualification', related_name='qualification')
    # #Relational
    # profession = models.ManyToManyField(to='Profession', related_name='profession')
    # dob = models.DateField(max_length=120)
    # sex = models.CharField(max_length=120)
    # state = models.ForeignKey(to='State', related_name='state', on_delete=models.CASCADE)
    # lga = models.ForeignKey(to='Lga', related_name='lga', on_delete=models.CASCADE)
    # ward = models.ForeignKey(to='Ward', related_name='ward', on_delete=models.CASCADE)
    # polling_Unit = models.CharField(max_length=120)
    # geolocation = models.CharField(max_length=120)
    # #choices
    # prepared_State_of_To_Be_Involved = models.CharField(choices=state_choices, max_length=120)
    # prepared_Start_DateTobeInvolved = models.DateField(max_length=120)
    # prepared_EndDate_To_be_Involved = models.DateField(max_length=120)
    # #Choices
    # prepared_Days_To_be_Involved = models.CharField(choices=preparedDaysTobeInvolved_choices, max_length=120)
    # # preparedStartTimeTobeInvolved = models.TimeField(blank=True)
    # # preparedEndTimeTobeInvolved = models.TimeField(blank=True)
    # email = models.EmailField(unique=True)
    # phone_Number = models.CharField(max_length=120)
    # date_Of_Entry = models.DateField(max_length=120)
    # specialization = models.ManyToManyField(to='Specialization', related_name='specialazation', blank=True)
    # picture = models.ImageField(upload_to="volunteer/", blank=True)

    # def __str__(self):
    #     return self.first_Name




class Qualification(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
class Profession(models.Model):
    name = models.CharField(max_length=120)
    
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




















