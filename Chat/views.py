from django.http import HttpResponse
from django.template import loader
from backend.models import ExpiredKey
from django.http import Http404
from zlib import crc32

# Crc Hashing Library
P_32 = 0xEDB88320
init = 0xffffffff
_ran = True
tab32 = []

def mask32(n):
    return n & 0xffffffff

def mask8(n):
    return n & 0x000000ff

def mask1(n):
    return n & 0x00000001

def init32():
    for i in range(256):
        crc = mask32(i)
        for j in range(8):
            if (mask1(crc) == 1):
                crc = mask32(mask32(crc >> 1) ^ P_32)
            else:
                crc = mask32(crc >> 1)
        tab32.append(crc)
    global _ran
    _ran = False

def update32(crc, char):
    char = mask8(char)
    t = crc ^ char
    crc = mask32(mask32(crc >> 8) ^ tab32[mask8(t)])
    return crc

def runCRC(string):
    if _ran:
        init32()
    crc = init
    for c in string:
        crc = update32(crc, ord(c))
    crc = crc ^ init
    return hex(crc)[2:]

# The chatting frontend
def index(request):
    hash = request.GET.get('hash', None)
    key = request.GET.get('key', None)
    print("validating key: ", hash)
    expiredKeys = list(ExpiredKey.objects.values_list('key', flat=True))
    for i in expiredKeys:
        if hash == i:
            print("Invalid Key Found, raising 404...")
            raise Http404
        elif runCRC(key) != hash:
            print("Unmatching Key & Hash Found, raising 404...")
            raise Http404


    print("logging key: ", hash)
    currentKey = ExpiredKey(key=hash)
    currentKey.save()
    template = loader.get_template("Chat/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

