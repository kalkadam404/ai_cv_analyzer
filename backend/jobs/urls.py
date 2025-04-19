from django.urls import path
from .views import JobListingView

urlpatterns = [
    path('list/', JobListingView.as_view(), name='job_list'),
]
