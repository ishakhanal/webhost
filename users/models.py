from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    citizenship_number = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='profile_image' , blank=True)
    citizenship_image = models.ImageField(upload_to='id_image' , blank=True)
    approved_profile = models.BooleanField(default=False)

    def __str__(self):
    	return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Usermessage(models.Model):
    message_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    user_message = models.TextField()
    admin_reply = models.TextField(blank=True)
    send_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.message_creator)

class Notification(models.Model):
    message_receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    admin_message = models.TextField()
    notification_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.message_receiver)