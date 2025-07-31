from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Application
from django.http import HttpResponseForbidden

# EMPLOYER: View applications for a specific job
@login_required
def job_applications_view(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user)
    applications = Application.objects.filter(job=job)
    return render(request, 'employer/job_applications.html', {'job': job, 'applications': applications})

# EMPLOYER: Update application status
@login_required
def update_application_status(request, app_id, new_status):
    application = get_object_or_404(Application, id=app_id)
    if application.job.employer != request.user:
        return HttpResponseForbidden()
    if new_status in ['approved', 'rejected']:
        application.status = new_status
        application.save()
    return redirect('job_applications', job_id=application.job.id)

# APPLICANT: View and filter applications by status
@login_required
def applicant_dashboard(request):
    status_filter = request.GET.get('status')
    applications = Application.objects.filter(applicant=request.user)
    if status_filter in ['pending', 'approved', 'rejected']:
        applications = applications.filter(status=status_filter)
    return render(request, 'applicant/dashboard.html', {'applications': applications, 'status_filter': status_filter})
