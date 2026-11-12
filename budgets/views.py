from django.shortcuts import render
from django.db.models import Sum
from .models import BudgetAllocation, FinancialYear, Department, BudgetSector
from projects.models import DevelopmentProject, ProjectUpdate
import json

def home(request):
    current_year = FinancialYear.objects.filter(is_current=True).first()
    allocations = BudgetAllocation.objects.filter(financial_year=current_year) if current_year else BudgetAllocation.objects.none()
    totals = allocations.aggregate(allocated=Sum("approved_amount"), spent=Sum("actual_expenditure"))
    allocated = totals["allocated"] or 0
    spent = totals["spent"] or 0
    utilization = round(float(spent / allocated * 100), 1) if allocated else 0
    projects = DevelopmentProject.objects.all()[:5]
    updates = ProjectUpdate.objects.select_related("project").all()[:3]
    sector_rows = []
    for sector in BudgetSector.objects.all():
        row = allocations.filter(sector=sector).aggregate(
            allocated=Sum("approved_amount"), spent=Sum("actual_expenditure")
        )
        if row["allocated"] is not None:
            sector_rows.append({"name": sector.name, "allocated": float(row["allocated"]), "spent": float(row["spent"] or 0)})
    context = {
        "current_year": current_year, "allocated": allocated, "spent": spent,
        "utilization": utilization, "project_count": DevelopmentProject.objects.count(),
        "active_count": DevelopmentProject.objects.filter(status__in=["planned", "ongoing"]).count(),
        "completed_count": DevelopmentProject.objects.filter(status="completed").count(),
        "sector_rows": sector_rows, "projects": projects,
        "updates": updates,
    }
    return render(request, "home.html", context)



def budget_overview(request):
    years = FinancialYear.objects.all()
    selected = request.GET.get("year")

    year = (
        FinancialYear.objects.filter(pk=selected).first()
        if selected
        else years.filter(is_current=True).first()
    )

    allocations = (
        BudgetAllocation.objects.filter(financial_year=year)
        .select_related("department", "sector")
        if year
        else BudgetAllocation.objects.none()
    )

    totals = allocations.aggregate(
        total_approved=Sum("approved_amount"),
        total_revised=Sum("revised_amount"),
        total_spent=Sum("actual_expenditure"),
    )

    sector_rows = allocations.values("sector__name").annotate(
        approved=Sum("approved_amount"),
        revised=Sum("revised_amount"),
        spent=Sum("actual_expenditure"),
    ).order_by("sector__name")

    chart_data = {
        "labels": [row["sector__name"] for row in sector_rows],
        "approved": [float(row["approved"] or 0) for row in sector_rows],
        "revised": [float(row["revised"] or 0) for row in sector_rows],
        "spent": [float(row["spent"] or 0) for row in sector_rows],
    }

    context = {
        "years": years,
        "selected_year": year,
        "allocations": allocations,
        "total_approved": totals["total_approved"] or 0,
        "total_revised": totals["total_revised"] or 0,
        "total_spent": totals["total_spent"] or 0,
        "chart_data": chart_data,
    }

    return render(request, "budgets/overview.html", context)

