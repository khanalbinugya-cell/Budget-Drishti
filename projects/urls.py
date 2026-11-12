from django.urls import path
from . import views

urlpatterns = [
    path("official-dashboard/", views.official_dashboard, name="official_dashboard"),
    path("", views.project_list, name="project_list"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("<int:pk>/update/", views.add_update, name="add_project_update"),
]