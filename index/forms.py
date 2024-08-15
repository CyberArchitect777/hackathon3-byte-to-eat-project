from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.Select(
            attrs={'class': 'form-control dropdown-arrow'}
        )
    )

    class Meta:
        model = Review
        fields = ('review_title', 'review_content', 'rating',)
        widgets = {
            'review_title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your review title'
                }
            ),
            'review_content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write your review here'
                }
            ),
        }
