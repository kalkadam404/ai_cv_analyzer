from django.contrib import admin
from .models import User  # или какая у тебя модель пользователя

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'date_joined')  # Какие поля будут отображаться
    list_filter = ('role', 'is_active')  # Фильтры по этим полям
    search_fields = ('username', 'email')  # Поиск по этим полям

# Регистрируем модель User в админке
admin.site.register(User, UserAdmin)
