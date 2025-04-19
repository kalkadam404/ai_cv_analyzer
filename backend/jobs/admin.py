from django.contrib import admin
from .models import Vacancy

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'posted_by', 'created_at', 'is_active')
    search_fields = ('title', 'company')
    list_filter = ('is_active',)
