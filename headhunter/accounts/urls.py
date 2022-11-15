from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, EmployerDetailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    # path('employer/profile/<int:pk>', EmployerDetailView.as_view(), name='employer_profile'),
    path('profile/<int:pk>', EmployerDetailView.as_view(template_name='employer_profile.html'), name='employer_profile')
]
