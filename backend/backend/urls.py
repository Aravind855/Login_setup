from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("storytelling/", include("storyTelling.urls", namespace="storyTelling")),
    path("api/", include("admin_portal.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
