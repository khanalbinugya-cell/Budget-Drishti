from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import CitizenInquiry, InquiryResponse
from .forms import InquiryForm
from django.views.decorators.http import require_POST

@login_required
def inquiry_create(request):
    form = InquiryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        inquiry = form.save(commit=False)
        inquiry.citizen = request.user
        inquiry.save()
        messages.success(request, "Your inquiry has been submitted.")
        return redirect("my_inquiries")
    return render(request, "inquiries/inquiry_form.html", {"form": form})

@login_required
def my_inquiries(request):
    if request.user.role == "admin":
        inquiries = CitizenInquiry.objects.all()
    elif request.user.role == "official":
        inquiries = CitizenInquiry.objects.filter(Q(project__department=request.user.department) | Q(project__isnull=True))
    else:
        inquiries = CitizenInquiry.objects.filter(citizen=request.user)
    return render(request, "inquiries/inquiry_list.html", {"inquiries": inquiries})

@login_required
def inquiry_respond(request, pk):
    if request.user.role not in ["official", "admin"]:
        messages.error(request, "Only officials can respond.")
        return redirect("my_inquiries")
    inquiry = get_object_or_404(CitizenInquiry, pk=pk)
    if request.user.role == "official" and inquiry.project and inquiry.project.department_id != request.user.department_id:
        messages.error(request, "This inquiry is not assigned to your department.")
        return redirect("my_inquiries")
    if request.method == "POST":
        response = request.POST.get("response", "").strip()
        if response:
            InquiryResponse.objects.create(inquiry=inquiry, official=request.user, response=response)
            inquiry.status = "answered"
            inquiry.save(update_fields=["status"])
            messages.success(request, "Response published.")
        return redirect("my_inquiries")
    return render(request, "inquiries/respond.html", {"inquiry": inquiry})

@login_required
@require_POST
def inquiry_delete(request, pk):
    inquiry = get_object_or_404(
        CitizenInquiry,
        pk=pk,
        citizen=request.user,
        status="open"
    )

    inquiry.delete()
    messages.success(request, "Your inquiry has been deleted.")

    return redirect("my_inquiries")

