from django.db import models




class ReportCase(models.Model):
    first_Name = models.CharField(max_length=120)
    middle_Name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    sex = models.CharField(max_length=120)
    state = models.ForeignKey(to='State', related_name='reportCases', on_delete=models.CASCADE)
    lga = models.ForeignKey(to='Lga', related_name='reportCases', on_delete=models.CASCADE)
    ward = models.ForeignKey(to='Ward', related_name='reportCases', on_delete=models.CASCADE)
    polling_Unit = models.CharField(max_length=120)
    geolocation = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone_Number = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True, default='')
    reportDate = models.DateField(max_length=120)

    def __str__(self):
        return self.first_Name


class Volunteer(models.Model):
    preparedDaysTobeInvolved_choices = (
        ('monday', "Monday"),
        ('tuesday', "Tuesday"),
        ('sunday', "Sunday"),
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

    ##Auto Generated Field
    entryID = models.CharField(max_length=120, blank=True, default='')
    def save(self, force_insert=False, force_update=False):
        if self.entryID == "":
            existing_entryIDs = Volunteer.objects.all().order_by('-entryID')
            if existing_entryIDs.count() > 0:
                new_entryID = int(existing_entryIDs[0].code[1:]) + 1
            else:
                new_entryID = 0
            self.entryID = 'E%03d' % new_entryID
        super(Volunteer, self).save(force_insert, force_update)

    # ##Auto Generated Field
    # involvementID = models.CharField(max_length=120, blank=True, default='')
    # def push(self, force_insert=False, force_update=False):
    #     if self.involvementID == "":
    #         existing_involvementIDs = Volunteer.objects.all().order_by('-involvementID')
    #         if existing_involvementIDs.count() > 0:
    #             new_involvementID = int(existing_involvementIDs[0].code[1:]) + 1
    #         else:
    #             new_involvementID = 0
    #         self.involvementID = 'I%03d' % new_involvementID
    #     super(Volunteer, self).save(force_insert, force_update)

    first_Name = models.CharField(max_length=120)
    middle_Name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    ##Relational
    highest_Qualification = models.ManyToManyField(to='HighestQualification', related_name='volunteers')
    #Relational
    profession = models.ManyToManyField(to='Profession', related_name='volunteers')
    dob = models.DateField(max_length=120)
    sex = models.CharField(max_length=120)
    state = models.ForeignKey(to='State', related_name='volunteers', on_delete=models.CASCADE)
    lga = models.ForeignKey(to='Lga', related_name='volunteers', on_delete=models.CASCADE)
    ward = models.ForeignKey(to='Ward', related_name='volunteers', on_delete=models.CASCADE)
    polling_Unit = models.CharField(max_length=120)
    geolocation = models.CharField(max_length=120)
    #choices
    prepared_State_of_To_Be_Involved = models.CharField(choices=state_choices, max_length=120)
    prepared_Start_DateTobeInvolved = models.DateField(max_length=120)
    prepared_EndDate_To_be_Involved = models.DateField(max_length=120)
    #Choices
    prepared_Days_To_be_Involved = models.CharField(choices=preparedDaysTobeInvolved_choices, max_length=120)
    # preparedStartTimeTobeInvolved = models.TimeField(blank=True)
    # preparedEndTimeTobeInvolved = models.TimeField(blank=True)
    email = models.EmailField(unique=True)
    phone_Number = models.CharField(max_length=120)
    date_Of_Entry = models.DateField(max_length=120)
    specialization = models.ManyToManyField(to='Specialization', related_name='volunteers', blank=True)
    picture = models.ImageField(upload_to="volunteer/", blank=True)

    def __str__(self):
        return self.first_Name

class HighestQualification(models.Model):
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




















