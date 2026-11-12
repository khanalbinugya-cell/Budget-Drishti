from django.urls import path
from .views import budget_overview
urlpatterns = [path("", budget_overview, name="budget_overview")]
