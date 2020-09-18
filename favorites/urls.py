from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtofavoritecart/<int:id>', views.addtofavoritecart, name='addtofavoritecart'),
    path('deletefromfavoritecart/<int:id>', views.deletefromfavoritecart, name='deletefromfavoritecart'),

]