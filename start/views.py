from django.http import HttpResponse
from django.template import loader

# The start page
def index(request):
    template = loader.get_template("start/index.html")
    context = {}
    return HttpResponse(template.render(context, request))
