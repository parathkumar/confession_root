from django.db import models
from django.contrib.auth.models import User

class posts(models.Model):
    title      = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=50)
    content    = models.TextField(max_length=100000)
    #comments   = models.CharField(max_length=500,default="Your thoughts here")
    #opinion    = models.BooleanField(default=True,null=False)
    #picture    = models.ImageField(upload_to="pictures/",default="/pictures/pict.jpg")
    author     =  models.ForeignKey(User,on_delete=models.CASCADE,default=None)


    def __str__(self):
        return self.title