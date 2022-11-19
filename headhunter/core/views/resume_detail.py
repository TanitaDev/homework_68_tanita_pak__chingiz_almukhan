from django.contrib.auth import get_user_model
from django.views.generic import DetailView

from core.models import Resume, Education, Job


class ResumeDetailView(DetailView):
    model = Resume
    template_name = "resume_detail.html"
    context_object_name = 'resume'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # user = self.get_object()
        # resume = Resume.objects.filter(pk=self.object.pk)
        print(self.object.pk)
        context['education'] = Education.objects.filter(resume_id=self.object.pk)
        context['job'] = Job.objects.filter(resume_id=self.object.pk)
        return context
