from django.contrib import admin

from .models import PrimaryKey, SecondaryKey, NotAKey


admin.site.register(PrimaryKey)
admin.site.register(SecondaryKey)
admin.site.register(NotAKey)
