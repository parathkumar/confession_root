from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Display_Picture = models.ImageField(upload_to='pictures',default="/pictures/pict.jpg")

    def __str__(self):
        return self.user.username

@receiver(signal=post_save,sender = User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)