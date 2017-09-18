from django.http import HttpResponse
from django.template import loader
from backend.models import ExpiredKey
from django.http import Http404

# The chatting frontend
def index(request, hash):
    print("validating key: ", hash)
    expiredKeys = list(ExpiredKey.objects.values_list('key', flat=True))
    for i in expiredKeys:
        if hash == i:
            print("Invalid Key Found, raising 404...")
            raise Http404

    print("logging key: ", hash)
    currentKey = ExpiredKey(key=hash)
    currentKey.save()
    template = loader.get_template("Chat/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

