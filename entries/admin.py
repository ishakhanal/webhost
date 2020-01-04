from django.contrib import admin

from .models import Contract, Comment

# Register your models here.
admin.site.register(Contract)
admin.site.register(Comment)