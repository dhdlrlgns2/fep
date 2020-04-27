from django.contrib import admin
from django.urls import path, include
import base.views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#accounts/login/social/naver/callback/
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
