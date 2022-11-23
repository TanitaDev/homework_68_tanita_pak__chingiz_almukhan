from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView

from accounts.forms import CustomUserCreationForm, LoginForm
from accounts.models import Profile
from core.models import Resume, Vacancy
from django.core.paginator import Paginator


class IndexView(ListView):
    template_name = 'index.html'
    paginate_by = 1
    model = Vacancy
    context_object_name = 'vacancy'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['register_form'] = CustomUserCreationForm()
        context['login_form'] = LoginForm()
        return context

    def get_queryset(self):
        return Vacancy.objects.filter(is_active=False).order_by('-updated_at')


def update_resume(request, *args, **kwargs):
    resume = get_object_or_404(Resume, pk=kwargs['pk'])
    resume.updated_at = timezone.now()
    resume.save()
    return redirect('employer_profile', pk=resume.author_id)
