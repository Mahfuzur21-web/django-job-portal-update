# jobs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('employer/job/<int:job_id>/applications/', views.job_applications_view, name='job_applications'),
    path('application/<int:app_id>/update/<str:new_status>/', views.update_application_status, name='update_application_status'),
    path('applicant/dashboard/', views.applicant_dashboard, name='applicant_dashboard'),
]
