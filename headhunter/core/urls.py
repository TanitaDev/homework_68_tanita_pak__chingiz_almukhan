from django.urls import path

from core.views.add_resume_view import ResumeAddView, ResumeEditView, AddEducation, AddJob
from core.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('add/resume', ResumeAddView.as_view(), name='add_resume'),
    path('edit/resume/<int:pk>', ResumeEditView.as_view(), name='edit_resume'),
    path('resume/<int:pk>/add_education', AddEducation.as_view(), name='add_education'),
    path('resume/<int:pk>/add_job', AddJob.as_view(), name='add_job')
]
