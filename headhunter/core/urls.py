from django.urls import path

from core.views.base import IndexView
from core.views.vacancy import VacancyCreate, VacancyUpdate, VacancyDetail

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('vacancy/create', VacancyCreate.as_view(), name='vacancy_create'),
    path('vacancy/update/<int:pk>', VacancyUpdate.as_view(), name='vacancy_update')
]
