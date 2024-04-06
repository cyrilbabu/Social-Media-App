from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
    bio = models.TextField(max_length=500,blank=True)
    
    def __str__(self):
        return self.user.username