from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from budgets.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("accounts/", include("accounts.urls")),
    path("budgets/", include("budgets.urls")),
    path("projects/", include("projects.urls")),
    path("inquiries/", include("inquiries.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
