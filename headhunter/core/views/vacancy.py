from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from core.forms import VacancyForm
from core.models import Vacancy


class VacancyCreate(CreateView):
    template_name = "vacancy_create.html"
    form_class = VacancyForm
    model = Vacancy

    def get_success_url(self):
        return reverse('employer_profile', kwargs={'pk': self.object.pk})


class VacancyUpdate(UpdateView):
    template_name = "vacancy_update.html"
    form_class = VacancyForm
    model = Vacancy

    def get_success_url(self):
        return reverse('employer_profile', kwargs={'pk': self.object.pk})
