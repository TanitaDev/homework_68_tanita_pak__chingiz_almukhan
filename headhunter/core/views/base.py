from django.views.generic import ListView

from accounts.forms import CustomUserCreationForm, LoginForm
from accounts.models import Profile


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'something'
    model = Profile

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['register_form'] = CustomUserCreationForm()
        context['login_form'] = LoginForm()
        return context
