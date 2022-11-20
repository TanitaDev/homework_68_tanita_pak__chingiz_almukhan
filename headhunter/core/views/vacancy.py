from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from core.forms import VacancyForm
from core.models import Vacancy


class VacancyCreate(CreateView):
    template_name = "vacancy_create.html"
    form_class = VacancyForm
    model = Vacancy

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('employer_profile', kwargs={'pk': self.object.pk})


class VacancyUpdate(UpdateView):
    template_name = "vacancy_update.html"
    form_class = VacancyForm
    model = Vacancy

    def get_success_url(self):
        return reverse('employer_profile', kwargs={'pk': self.object.pk})


class VacancyDetail(DetailView):
    template_name = "vacancy_detail.html"
    model = Vacancy
    context_object_name = "vacancy"


def vacancy_reload(request, *args, **kwargs):
    vacancy = get_object_or_404(Vacancy, pk=kwargs['pk'])
    vacancy.updated_at = timezone.now()
    vacancy.save()

    return redirect('employer_profile', pk=vacancy.author_id)
