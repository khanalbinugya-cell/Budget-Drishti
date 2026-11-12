from django.contrib import admin
from .models import CitizenInquiry, InquiryResponse

admin.site.register(CitizenInquiry)
admin.site.register(InquiryResponse)