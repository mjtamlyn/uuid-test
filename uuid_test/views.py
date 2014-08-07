from django.shortcuts import render

from .models import PrimaryKey, SecondaryKey, NotAKey


def all_values(request):
    context = {
        'primary': PrimaryKey.objects.values(),
        'secondary': SecondaryKey.objects.values(),
        'not': NotAKey.objects.values(),
    }
    return render(request, 'all.html', context)
