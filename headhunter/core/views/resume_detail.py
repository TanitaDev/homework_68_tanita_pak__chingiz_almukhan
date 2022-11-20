import datetime

from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.http import HttpResponse
from django.views.generic import DetailView

from accounts.models import Profile
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


def download_pdf(request, *args, **kwargs):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Expenses' + \
                                      str(datetime.datetime.now()) + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    education = Education.objects.filter(resume_id=kwargs.get('pk'))
    job = Job.objects.filter(resume_id=kwargs.get('pk'))
    resume = Resume.objects.filter(pk=kwargs.get('pk'))
    to_str = resume.values('author')[0]
    check = to_str.get('author')
    author = Profile.objects.filter(pk=check)
    html_string = render_to_string('pdf_output.html',
                                   {'author': author, 'resume': resume, 'education': education, 'job': job})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf()
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response
