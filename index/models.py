from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField

# STATUS = ((0, "Draft"), (1, "Published"))


class Review(models.Model):
    """
    Stores or adds a review for a takeaway post.
    """

    FOOD_TYPE_CHOICES = [
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
    ]

    poster = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviewer"
    )
    takeaway_name = models.CharField(
        max_length=200
    )
    food_type = models.CharField(
        max_length=20,
        choices=FOOD_TYPE_CHOICES,
        default="Indian"
    )
    review_title = models.CharField(
        max_length=50
    )
    review_content = models.TextField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        default=3
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    edited_on = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["-created_on"]

    def __str__(self):
        return f"Review of {self.takeaway_name} by {self.poster}"
