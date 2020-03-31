from django.db import models



class Doctor(models.Model):
    name = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)
    picture = models.ImageField(upload_to="doctors/")
    details = models.TextField()
    experience = models.TextField()
    expertise = models.ManyToManyField(to='Expertise', related_name='doctors')
    twitter = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name


class Expertise(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name







# EntryID
# InvolvementID
# FirstName
# MiddleName
# Surname
# HighestQualification (SSCE, OND/ND,  B.Sc./B.Art/B.Ed/Btech/B.Eng/Etc., MSC/MBA/MPA/MPH/Etc. PhD/DBA/Etc. )
# Profession (Surgeon, Nurse, Anesthesia, Lab Scientist, Pharmacist, Health Record, Social Worker, Lawyer, IT and Data Analyst, Social Media, Accountant, Economist, etc)
# DoB
# Sex
# State
# LGA
# Ward
# PollingUnit
# Geolocation (Based on User map)
# PreparedStateofToBeInvolved
# PreparedStartDateTobeInvolved
# PreparedEndDateandTobeInvolved
# PreparedDaysTobeInvolved (Check Box: Mon, Tues, to Sunday)
# PreparedStartTimeTobeInvolved (From 00 to 24)
# PreparedEndTimeTobeInvolved (From 00 to 24)
# PhoneNo
# Email
# Address
# DateOfEntry








