from django.http import HttpResponse
from django.template import loader

# The chatting frontend
def index(request):
    template = loader.get_template("Chat/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

#
# def translate(request, translateValue):
#     responseHTML = ''
#     try:
#         result = TranslatorEntry.objects.filter(key=int(translateValue)).values_list("value", flat=True)[0]
#     except IndexError:
#         result = 'not found'
#     responseHTML += "<h3>Result: " + result + "</h3>"
#
#     return HttpResponse(responseHTML)

