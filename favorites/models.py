from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

from product.models import Product


class FavoriteCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product.title


class FavoriteCartForm(ModelForm):
    class Meta:
        model = FavoriteCart
        fields = ['product']