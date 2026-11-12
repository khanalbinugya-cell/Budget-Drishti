from django.db import models
from django.db.models import Sum

class Department(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    def __str__(self): return self.name

class FinancialYear(models.Model):
    name = models.CharField(max_length=20, unique=True)
    is_current = models.BooleanField(default=False)
    def __str__(self): return self.name

class BudgetSector(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    def __str__(self): return self.name

class BudgetAllocation(models.Model):
    financial_year = models.ForeignKey(FinancialYear, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    sector = models.ForeignKey(BudgetSector, on_delete=models.PROTECT)
    approved_amount = models.DecimalField(max_digits=14, decimal_places=2)
    revised_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    actual_expenditure = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    source_note = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sector__name"]
        unique_together = ("financial_year", "department", "sector")

    @property
    def utilization(self):
        if not self.approved_amount:
            return 0
        return round(float(self.actual_expenditure / self.approved_amount * 100), 1)

    @property
    def remaining(self):
        return self.approved_amount - self.actual_expenditure

    def __str__(self):
        return f"{self.financial_year} - {self.sector}"
