from django.db import models
from django.contrib.auth.models import User



class SiteUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    aadhar_no = models.CharField(max_length=12,null=True)
    email = models.EmailField(max_length=255)
    fname = models.CharField(max_length=100) 
    lname = models.CharField(max_length=100) 
    is_mentor = models.BooleanField(default=False)


    rank = models.CharField(max_length=100,null=True)
    photo = models.ImageField(upload_to='photos/',null=True)
    # aadhar = models.FileField(upload_to='aadhar/')

    def __str__(self):
        return self.user.username
        # return f'{self.fname} {self.lname}'