from django.db import models

# Create your models here.

# Model for About Page (details can be updated via the admin panel)
class About(models.Model):
    title = models.CharField(max_length=200)
    about_byte2eat = models.TextField()
    about_snackoverflow = models.TextField()

    def __str__(self):
        return self.title


#Model to add About us Cards (can be added via admin as well)

