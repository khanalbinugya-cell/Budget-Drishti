from django.db import models
from django.conf import settings
from projects.models import DevelopmentProject


class CitizenInquiry(models.Model):
    STATUS_CHOICES = [("open", "Open"), ("in_progress", "In progress"), ("answered", "Answered"), ("closed", "Closed")]
    citizen = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="inquiries")
    project = models.ForeignKey(DevelopmentProject, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.CharField(max_length=180)
    question = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.subject

class InquiryResponse(models.Model):
    inquiry = models.ForeignKey(CitizenInquiry, on_delete=models.CASCADE, related_name="responses")
    official = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
