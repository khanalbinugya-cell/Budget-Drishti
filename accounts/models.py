from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ("citizen", "Citizen"),
        ("official", "Department Official"),
        ("admin", "Administrator"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="citizen")
    department = models.ForeignKey(
        "budgets.Department", on_delete=models.SET_NULL,
        null=True, blank=True, related_name="officials"
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
