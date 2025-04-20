from django.urls import path
from .views import ResumeFeedbackView

urlpatterns = [   
    path('feedback/<int:resume_id>/', ResumeFeedbackView.as_view(), name='resume_feedback'),
]
