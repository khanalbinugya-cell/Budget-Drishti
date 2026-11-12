from django.contrib import admin
from .models import Department, FinancialYear, BudgetSector, BudgetAllocation

admin.site.register(Department)
admin.site.register(FinancialYear)
admin.site.register(BudgetSector)
admin.site.register(BudgetAllocation)