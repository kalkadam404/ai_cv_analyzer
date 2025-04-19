from rest_framework import serializers
from .models import JobListing, Vacancy

class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = ['title', 'description', 'location', 'skills_required', 'posted_by', 'posted_at']
        
class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'
