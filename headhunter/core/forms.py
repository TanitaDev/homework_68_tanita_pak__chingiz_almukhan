from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from core.models import Resume, Education, Job
from core.models import Vacancy


class RequiredFieldsModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequiredFieldsModelForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if (
                    hasattr(bound_field, "field") and
                    bound_field.name in self.Meta.required_fields
            ):
                bound_field.field.widget.attrs["required"] = "required"


class ResumeChangeForm(RequiredFieldsModelForm):
    # category = forms.ChoiceField(choices=CATEGORY, required=True)
    # telegram = forms.CharField(required=True)
    # email = forms.CharField(required=True)
    # phone_number = forms.CharField(required=True)

    class Meta:
        model = Resume
        fields = ('category', 'about', 'salary', 'telegram', 'email', 'phone_number', 'linkedin', 'facebook')
        required_fields = ['category', 'telegram', 'email', 'phone_number']


class DateInput(forms.DateInput):
    input_type = 'date'


class EducationAddEditForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput, label='Дата начала обучения')
    end_date = forms.DateField(widget=DateInput, label='Дата окончания обучения')

    class Meta:
        model = Education
        fields = ('study', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs.update(
            {'class': 'form-control', 'min': "2018-01-01", 'max': "2090-12-31", 'type': 'date'})
        self.fields['end_date'].widget.attrs.update(
            {'class': 'form-control', 'min': "2018-01-01", 'max': "2090-12-31", 'type': 'date'})


class JobAddEditForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput, label='Дата начала обучения')
    end_date = forms.DateField(widget=DateInput, label='Дата окончания обучения')

    class Meta:
        model = Job
        fields = ('description', 'company', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs.update(
            {'class': 'form-control', 'min': "2018-01-01", 'max': "2090-12-31", 'type': 'date'})
        self.fields['end_date'].widget.attrs.update(
            {'class': 'form-control', 'min': "2018-01-01", 'max': "2090-12-31", 'type': 'date'})


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'salary', 'description', 'experience', 'category', 'is_active']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Поиск вакансий")
