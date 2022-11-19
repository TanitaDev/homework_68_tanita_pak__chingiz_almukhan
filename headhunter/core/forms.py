from django import forms

from core.models import Vacancy


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'salary', 'description', 'experience', 'category']
