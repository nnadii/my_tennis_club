from django.http import HttpResponse
from django.template import loader

# Create your views here.


def members(request):
    template = loader.get_template("my_first.html")
    return HttpResponse(template.render())
