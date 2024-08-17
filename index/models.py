from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField

# STATUS = ((0, "Draft"), (1, "Published"))


# class Takeaway(models.Model):
#     """
#     Stores a single takeaway on the below details.
#     """
#     takeaway_name = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     food_type = models.CharField(max_length=50, unique=False)
#     address = models.CharField(max_length=50)
#     content = models.TextField()
#     image = CloudinaryField('image', default='placeholder')
#     status = models.IntegerField(choices=STATUS, default=0)

#     class Meta:
#         ordering = ["takeaway_name"]


class Review(models.Model):
    """
    Stores/Adds a review to the takeaway post
    """

    FOOD_TYPE_CHOICES = [
("Chinese", "Chinese"),
("Curry", "Curry"),
("Pizza", "Pizza"),
("Sushi", "Sushi"),
("Burgers", "Burgers"),
("Fish & Chips", "Fish & Chips"),
("Other", "Other"),
    ] # Can add more food choice options here in the future

    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    takeaway_name = models.CharField(max_length=200, unique=False)
    food_type = models.IntegerField(choices=FOOD_TYPE_CHOICES, default=Chinese) # Default choice would be Chinese - user can just select from drop down menu)
    review_title = models.CharField(max_length=50, unique=False)
    review_content = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=3
    )
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Review of {self.takeaway_name} by {self.poster}"