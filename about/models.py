from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

# Model for About Page (details can be updated via the admin panel)
class About(models.Model):
    title = models.CharField(max_length=200)
    about_byte2eat = models.TextField()
    about_snackoverflow = models.TextField()

    def __str__(self):
        return self.title


#Model to add About us Cards (can be added via admin as well)

class Snack_Profile(models.Model):
    """
    Stores a single admin user for About US profile using the below details
    """
    profile_name = models.CharField(max_length=200, unique=True)
    about_profile = models.CharField(max_length=200, unique=False)
    funfact = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["profile_name"]