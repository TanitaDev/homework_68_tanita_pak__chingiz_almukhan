from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView

from accounts.forms import LoginForm, CustomUserCreationForm
from accounts.models import Profile


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('main')
        password = form.cleaned_data.get('password')
        if '@' not in form.cleaned_data.get('email'):
            phone = form.cleaned_data.get('email')
            email = Profile.objects.filter(phone_number=phone).values('email')
            if len(email) == 0:
                return redirect('main')
            email_str = email[0]
            user = authenticate(request, email=email_str.get('email'), password=password)
            if not user:
                return redirect('main')
            login(request, user)
            return redirect('ready')
        email = form.cleaned_data.get('email')
        user = authenticate(request, email=email, password=password)
        if not user:
            return redirect('main')
        login(request, user)
        return redirect('main')


def logout_view(request):
    logout(request)
    return redirect('main')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
        context = {}
        context['form'] = form
        return self.render_to_response(context)

