from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, F, Sum, Avg
from django.db.models.signals import post_save
from django.urls import reverse_lazy
from PIL import Image

from blog.models import *


class Profile(models.Model):
    GENDER_CHOICES = (
        (None, 'Choose your gender'),
        ('male', 'male'),
        ('female', 'female'),
        ('custom', 'custom'),
        ('Prefer Not To Say', 'Prefer Not To Say'),
    )

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=200, null=True)
    bio = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='male', verbose_name="gender")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse_lazy("user-detail", kwargs={"username": self.user.username})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


def create_profile(sender, **kwarg):
    if kwarg['created']:
        Profile.objects.create(user=kwarg['instance'])


post_save.connect(create_profile, sender=User)



