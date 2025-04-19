from django.contrib import admin
from .models import Resume

class ResumeAdmin(admin.ModelAdmin):
    list_display = ['user', 'file', 'extracted_text', 'skills', 'education', 'experience', 'uploaded_at']  # Здесь ты показываешь нужные поля резюме
    list_filter = ('user', 'uploaded_at')  # Фильтры для удобного поиска
    search_fields = ('user__username', 'file')  # Возможность поиска по имени пользователя и файлу

# Регистрируем модель Resume в админке
admin.site.register(Resume, ResumeAdmin)
