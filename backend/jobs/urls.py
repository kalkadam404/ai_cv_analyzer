from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VacancyViewSet, analytics_view, recommended_vacancies

router = DefaultRouter()
router.register('vacancies', VacancyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vacancies/recommended/', recommended_vacancies),
    path('analytics/', analytics_view),
]
