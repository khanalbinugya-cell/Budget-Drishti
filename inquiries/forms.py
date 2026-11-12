from django import forms
from .models import CitizenInquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = CitizenInquiry
        fields = ["project", "subject", "question"]
        widgets = {"question": forms.Textarea(attrs={"rows": 5})}
