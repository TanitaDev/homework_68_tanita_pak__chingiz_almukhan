from django.core.serializers import serialize
from django.http import JsonResponse

from core.models import Vacancy


def vacancy_list_view(request, *args, **kwargs):
    if request.method == "GET":
        search = request.GET.get('search')
        print(search)
        return JsonResponse(serialize('json', Vacancy.objects.filter(name__icontains=search)), safe=False)
