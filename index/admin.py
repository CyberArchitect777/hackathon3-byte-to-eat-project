
from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin


# @admin.register(Takeaway)
# class TakeawayAdmin(SummernoteModelAdmin):
#     list_display = ('takeaway_name', 'slug', 'status')
#     search_fields = ['takeaway_name', 'content', ]
#     list_filter = ('status',)
#     prepopulated_fields = {'slug': ('takeaway_name',)}
#     summernote_fields = ('content',)


# Register your models here.
admin.site.register(Review)