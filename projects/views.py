from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import DevelopmentProject
from .forms import ProjectUpdateForm
from inquiries.models import CitizenInquiry
from django.db.models import Sum, Avg, Q

def project_list(request):
    projects = DevelopmentProject.objects.select_related("department", "sector")
    return render(request, "projects/project_list.html", {"projects": projects})

def project_detail(request, pk):
    project = get_object_or_404(DevelopmentProject, pk=pk)
    return render(request, "projects/project_detail.html", {"project": project})

def is_official(user):
    return user.is_authenticated and user.role in ["official", "admin"]


@login_required
@user_passes_test(is_official)
@login_required
@user_passes_test(is_official)
def official_dashboard(request):
    if request.user.role == "official":
        projects = DevelopmentProject.objects.filter(
            department=request.user.department
        ).select_related("department", "sector")

        inquiries = CitizenInquiry.objects.filter(
            Q(project__department=request.user.department) |
            Q(project__isnull=True)
        ).select_related("citizen", "project")

    else:
        projects = DevelopmentProject.objects.all().select_related(
            "department", "sector"
        )
        inquiries = CitizenInquiry.objects.all().select_related(
            "citizen", "project"
        )

    total_projects = projects.count()
    total_inquiries = inquiries.count()

    pending_inquiries = inquiries.filter(
        status__in=["open", "in_progress"]
    ).count()

    answered_inquiries = inquiries.filter(status="answered").count()

    average_progress = projects.aggregate(
        average=Avg("physical_progress")
    )["average"] or 0

    total_budget = projects.aggregate(
        total=Sum("allocated_budget")
    )["total"] or 0

    total_expenditure = projects.aggregate(
        total=Sum("actual_expenditure")
    )["total"] or 0

    recent_inquiries = inquiries.order_by("-created_at")[:5]

    context = {
        "projects": projects,
        "total_projects": total_projects,
        "total_inquiries": total_inquiries,
        "pending_inquiries": pending_inquiries,
        "answered_inquiries": answered_inquiries,
        "average_progress": round(average_progress, 1),
        "total_budget": total_budget,
        "total_expenditure": total_expenditure,
        "recent_inquiries": recent_inquiries,
    }

    return render(request, "projects/official_dashboard.html", context)
@login_required
@user_passes_test(is_official)
def add_update(request, pk):
    project = get_object_or_404(DevelopmentProject, pk=pk)
    if request.user.role == "official" and request.user.department_id != project.department_id:
        messages.error(request, "You can only update projects assigned to your department.")
        return redirect("project_detail", pk=pk)
    form = ProjectUpdateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        update = form.save(commit=False)
        update.project = project
        update.created_by = request.user
        update.save()
        project.physical_progress = update.physical_progress
        project.actual_expenditure = update.expenditure_to_date
        if project.physical_progress >= 100:
            project.status = "completed"
        elif project.status == "planned":
            project.status = "ongoing"
        project.save()
        messages.success(request, "Project update saved.")
        return redirect("project_detail", pk=pk)
    return render(request, "projects/update_form.html", {"form": form, "project": project})
