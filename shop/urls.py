from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    path('', include('core.urls')),
    path('home/', include('core.urls')),
    path('about/', views.aboutus, name='aboutus'),
    path('product/', include('product.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
