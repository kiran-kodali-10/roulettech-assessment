from django.contrib import admin
from .models import Person, Company

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'date', 'location', 'position_title')
    search_fields = ('company_name', 'location', 'position_title')
