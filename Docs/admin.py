from django.contrib import admin
from Docs.models import Doc

@admin.register(Doc)
class MyAdmin(admin.ModelAdmin):
    pass
