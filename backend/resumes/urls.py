from django.urls import path
from .views import ResumeDetailView, ResumeListView, ResumeUploadView

urlpatterns = [
    path('resumes/upload/', ResumeUploadView.as_view(), name='resume_upload'),
    path('resumes/', ResumeListView.as_view(), name='resume_list'),
    path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume_detail'),
]
