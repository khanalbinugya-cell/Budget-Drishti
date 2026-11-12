from django import forms
from .models import ProjectUpdate

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = ProjectUpdate
        fields = ["physical_progress", "expenditure_to_date", "remarks"]
