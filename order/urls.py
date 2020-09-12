from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name='order'),
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),

]