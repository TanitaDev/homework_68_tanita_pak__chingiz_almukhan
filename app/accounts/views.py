from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView


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
            return redirect('login')
        password = form.cleaned_data.get('password')
        if '@' not in form.cleaned_data.get('email'):
            phone = form.cleaned_data.get('email')
            email = User.objects.filter(username=phone).values('email')
            if len(email) == 0:
                return redirect('login')
            username_str = email[0]
            user = authenticate(request, username=username_str.get('username'), password=password)
            if not user:
                return redirect('login')
            login(request, user)
            return redirect('main')
        email = form.cleaned_data.get('email')
        user = authenticate(request, email=email, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        return redirect('main')


def logout_view(request):
    logout(request)
    return redirect('login')


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
