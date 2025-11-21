from django.contrib import admin
from .models import UserRegister

@admin.register(UserRegister)
class UserRegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age', 'is_active', 'dob', 'gender')
    list_filter = ('is_active', 'gender')
    search_fields = ('name', 'email')
