
from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_inquiries, name="my_inquiries"),
    path("new/", views.inquiry_create, name="inquiry_create"),
    path("<int:pk>/respond/", views.inquiry_respond, name="inquiry_respond"),
    path("<int:pk>/delete/", views.inquiry_delete, name="inquiry_delete"),
]
