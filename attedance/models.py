from django.db import models

# student model
class student(models.Model):
  first_name = models.CharField(max_length =30)
  last_name = models.CharField(max_length =30)
  email = models.EmailField()  
  status = models.TextField(max_length = 30, blank = True)
  phone_number = models.IntegerField(blank =True, null = True)
  profile_pic = models.ImageField(upload_to = 'profile_pic/', null =True, blank = True)
