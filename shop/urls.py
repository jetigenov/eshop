from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

import core
from core import views

from order import views as OrderViews
from user import views as UserViews
from favorites import views as FavoriteViews


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('home/', include('core.urls')),
    path('product/', include('product.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('order/', include('order.urls')),
    path('user/', include('user.urls')),
    path('favorites/', include('favorites.urls')),

    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contactus, name='contactus'),

    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),

    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),

    path('shopcart/', OrderViews.shopcart, name='shopcart'),
    path('favoritecart/', FavoriteViews.favoritecart, name='favoritecart'),
    path('orders/', UserViews.user_orders, name='user_orders'),

    path('login/', UserViews.login_form, name='login_form'),
    path('logout/', UserViews.logout_func, name='logout_func'),
    path('signup/', UserViews.signup_form, name='signup_form'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
        name="password_reset_complete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
