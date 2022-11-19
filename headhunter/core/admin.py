from django.contrib import admin
from core.models import Vacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Vacancy, VacancyAdmin)
