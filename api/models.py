from django.db import models

# Create your models here.
# UserInformation class that will create new student's details
class UserInformation(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    Day = models.DateField()
    gender = models.CharField(max_length=10)
    status= models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to = 'profile_pic/', null =True, blank = True)
    phone_number = models.IntegerField(blank =True, null = True)
    email = models.EmailField(blank =True, null = True)  



