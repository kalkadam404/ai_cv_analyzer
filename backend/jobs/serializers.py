from rest_framework import serializers
from .models import JobListing

class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = ['title', 'description', 'location', 'skills_required', 'posted_by', 'posted_at']
