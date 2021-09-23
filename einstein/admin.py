from django.contrib import admin

from . models import Language, Narrative, Topic, models

admin.site.register(Language)
admin.site.register(Topic)
admin.site.register(Narrative)
