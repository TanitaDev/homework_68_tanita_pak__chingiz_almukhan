from django.urls import path

from core.views.add_resume_view import ResumeAddView, ResumeEditView, AddEducation, AddJob
from core.views.base import IndexView, update_resume
from core.views.resume_detail import ResumeDetailView, download_pdf
from core.views.vacancy import VacancyCreate, VacancyUpdate, VacancyDetail, vacancy_reload

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('add/resume', ResumeAddView.as_view(), name='add_resume'),
    path('edit/resume/<int:pk>', ResumeEditView.as_view(), name='edit_resume'),
    path('resume/<int:pk>/add_education', AddEducation.as_view(), name='add_education'),
    path('resume/<int:pk>/', ResumeDetailView.as_view(), name='resume_detail'),
    path('resume/<int:pk>/add_job', AddJob.as_view(), name='add_job'),
    path('resume/update/<int:pk>', update_resume, name='update'),
    path('resume/download/<int:pk>', download_pdf, name='download'),

    path('vacancy/create', VacancyCreate.as_view(), name='vacancy_create'),
    path('vacancy/update/<int:pk>', VacancyUpdate.as_view(), name='vacancy_update'),
    path('vacancy/<int:pk>', VacancyDetail.as_view(), name='vacancy_detail'),
    path('vacancy/reload/<int:pk>', vacancy_reload, name='reload'),

]
