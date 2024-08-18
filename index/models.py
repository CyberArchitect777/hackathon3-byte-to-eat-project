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

    FOOD_TYPE_CHOICES = [ # Ideally, this would be in a separate model with links to review
        ("Indian", "Indian"),
        ("Italian", "Italian"),
        ("Chinese", "Chinese"),
        ("Thai", "Thai"),
        ("Japanese", "Japanese"),
        ("Mexican", "Mexican"),
        ("British", "British"),
        ("French", "French"),
        ("Greek", "Greek"),
        ("American", "American"),
        ("Turkish", "Turkish"),
        ("Korean", "Korean"),
        ("Vietnamese", "Vietnamese"),
        ("Spanish", "Spanish"),
        ("Lebanese", "Lebanese"),
        ("Caribbean", "Caribbean"),
        ("Other", "Other"),
        
    ] # Can add more food choice options here in the future

    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer") #Unique poster/user id
    takeaway_name = models.CharField(max_length=200, unique=False) # User can enter their own custom name of a takeaway
    food_type = models.CharField(max_length=20, choices=FOOD_TYPE_CHOICES, default="Indian") # Default choice would be Chinese - user can just select from drop down menu)
    review_title = models.CharField(max_length=50, unique=False) # Title of review
    review_content = models.TextField() # Textfield where user can add their takeaway review
    rating = models.IntegerField( # User can add a star rating from 1-5
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=3
    )
    created_on = models.DateTimeField(auto_now_add=True) # Date review was created on
    edited_on = models.DateTimeField(auto_now_add=True) # Date review was edited on

    class Meta:
        verbose_name = "Review" # This is the label that'll show up on the admin panel
        verbose_name_plural = "Reviews" # Same as above, just plural
        ordering = ["-created_on"] # Order reviews by date created on

    def __str__(self):
        return f"Review of {self.takeaway_name} by {self.poster}"