from django.contrib import admin
from backend.models import QAPairEntry, TranslatorEntry, Class, ExpiredKey
# Register your models here.

admin.site.register(QAPairEntry)
admin.site.register(TranslatorEntry)
admin.site.register(Class)
admin.site.register(ExpiredKey)