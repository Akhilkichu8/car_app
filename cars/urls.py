from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from .import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car_app/', include('car_app.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)