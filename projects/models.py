from django.db import models
from django.conf import settings
from budgets.models import Department, BudgetSector

class DevelopmentProject(models.Model):
    STATUS_CHOICES = [
        ("planned", "Planned"), ("ongoing", "Ongoing"),
        ("completed", "Completed"), ("delayed", "Delayed"),
    ]
    name = models.CharField(max_length=180)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    sector = models.ForeignKey(BudgetSector, on_delete=models.PROTECT)
    location = models.CharField(max_length=180)
    allocated_budget = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    actual_expenditure = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    physical_progress = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="planned")
    start_date = models.DateField(null=True, blank=True)
    expected_completion = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.name

class ProjectUpdate(models.Model):
    project = models.ForeignKey(DevelopmentProject, on_delete=models.CASCADE, related_name="updates")
    physical_progress = models.PositiveSmallIntegerField()
    expenditure_to_date = models.DecimalField(max_digits=14, decimal_places=2)
    remarks = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ["-created_at"]

class ProjectImage(models.Model):
    project = models.ForeignKey(DevelopmentProject, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="project_images/")
    caption = models.CharField(max_length=180, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
