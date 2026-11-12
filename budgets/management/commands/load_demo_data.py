from django.core.management.base import BaseCommand
from budgets.models import Department, FinancialYear, BudgetSector, BudgetAllocation
from projects.models import DevelopmentProject

class Command(BaseCommand):
    help = "Load clearly illustrative Sundarpur Municipality demo data"

    def handle(self, *args, **options):
        year, _ = FinancialYear.objects.get_or_create(name="2082/83", defaults={"is_current": True})
        FinancialYear.objects.exclude(pk=year.pk).update(is_current=False)
        year.is_current = True
        year.save()
        rows = [
            ("Education", 100, 70), ("Healthcare", 80, 55),
            ("Infrastructure", 150, 90), ("Agriculture", 70, 45),
            ("Sanitation", 50, 40), ("Other services", 50, 0),
        ]
        dept, _ = Department.objects.get_or_create(name="Municipal Development Department")
        for name, allocated, spent in rows:
            sector, _ = BudgetSector.objects.get_or_create(name=name)
            BudgetAllocation.objects.update_or_create(
                financial_year=year, department=dept, sector=sector,
                defaults={"approved_amount": allocated * 100000, "revised_amount": allocated * 100000,
                          "actual_expenditure": spent * 100000,
                          "source_note": "Illustrative sample data; not an official municipal record."}
            )
        sample_projects = [
            ("School Building Construction", "Construction of additional classrooms.", "Education", "Ward 2", 5000000, 3500000, 65, "ongoing"),
            ("Local Road Improvement", "Improvement of a local access road.", "Infrastructure", "Ward 4", 8000000, 3600000, 45, "ongoing"),
            ("Health Post Renovation", "Renovation of the local health post.", "Healthcare", "Ward 1", 3000000, 2700000, 90, "ongoing"),
            ("Drinking Water Project", "Improvement of community drinking water access.", "Infrastructure", "Ward 5", 6000000, 3000000, 60, "ongoing"),
            ("Community Sanitation Project", "Community sanitation improvement.", "Sanitation", "Ward 3", 2500000, 2500000, 100, "completed"),
        ]
        for name, desc, sector_name, location, budget, spent, progress, status in sample_projects:
            sector = BudgetSector.objects.get(name=sector_name)
            DevelopmentProject.objects.update_or_create(
                name=name,
                defaults={"description": desc, "department": dept, "sector": sector, "location": location,
                          "allocated_budget": budget, "actual_expenditure": spent,
                          "physical_progress": progress, "status": status}
            )
        self.stdout.write(self.style.SUCCESS("Illustrative demo data loaded."))
