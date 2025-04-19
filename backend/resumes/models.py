from django.db import models
from django.conf import settings

def resume_upload_path(instance, filename):
    return f'resumes/{instance.user.username}/{filename}'

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to=resume_upload_path)
    extracted_text = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s resume"
    
    @property
    def file_url(self):
        return self.file.url 


