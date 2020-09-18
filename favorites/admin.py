from django.contrib import admin

from favorites.models import FavoriteCart


class FavoriteCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user']
    list_filter = ['user']



admin.site.register(FavoriteCart, FavoriteCartAdmin)