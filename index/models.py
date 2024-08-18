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
        (0, "Indian"),
        (1, "Italian"),
        (2, "Chinese"),
        (3, "Thai"),
        (4, "Japanese"),
        (5, "Mexican"),
        (6, "British"),
        (7, "French"),
        (8, "Greek"),
        (9, "American"),
        (10, "Turkish"),
        (11, "Korean"),
        (12, "Vietnamese"),
        (13, "Spanish"),
        (14, "Lebanese"),
        (15, "Caribbean"),
        (16, "Other"),

        # (0, "Chinese"),
        # (1, "Curry"),
        # (2, "Pizza"),
        # (3, "Sushi"), # Barrie -> Tina: Can remove these if you are happy with my changes
        # (4, "Burgers"),
        # (5, "Fish & Chips"),
        # (6, "Other"),
        
    ] # Can add more food choice options here in the future

    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer") #Unique poster/user id
    takeaway_name = models.CharField(max_length=200, unique=False) # User can enter their own custom name of a takeaway
    food_type = models.IntegerField(choices=FOOD_TYPE_CHOICES, default=0) # Default choice would be Chinese - user can just select from drop down menu)
    review_title = models.CharField(max_length=50, unique=False) # Title of review
    review_content = models.TextField() # Textfield where user can add their takeaway review
    rating = models.IntegerField( # User can add a star rating from 1-5
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=3
    )
    created_on = models.DateTimeField(auto_now_add=True) # Date review was created on
    edited_on = models.DateTimeField(auto_now_add=True) # Date review was edited on

    class Meta:
        ordering = ["-created_on"] # Order reviews by date created on

    def __str__(self):
        return f"Review of {self.takeaway_name} by {self.poster}"