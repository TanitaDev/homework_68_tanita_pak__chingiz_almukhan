from django.urls import path

from core.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
]