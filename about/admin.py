from django.contrib import admin
from .models import About, Snack_Profile
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('about_byte2eat, about_snackoverflow,')

@admin.register(Snack_Profile)
class Snack_ProfileAdmin(SummernoteModelAdmin):

    summernote_fields = ('about_profile, funfact,')