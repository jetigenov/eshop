from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import views
from order import views as OrderViews


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('home/', include('core.urls')),
    path('product/', include('product.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('order/', include('order.urls')),

    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contactus, name='contactus'),

    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),

    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),

    path('shopcart/', OrderViews.shopcart, name='shopcart'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
