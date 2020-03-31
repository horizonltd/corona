from django.db import models





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








