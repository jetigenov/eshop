from django.contrib import admin
from user.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'address', 'phone', 'city', 'country', 'image_tag']
    list_filter = ['city', 'country']


admin.site.register(UserProfile, UserProfileAdmin)
