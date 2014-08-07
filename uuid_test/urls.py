from django.conf.urls import include, url
from django.contrib import admin

from .views import all_values


urlpatterns = [
    url(r'^$', all_values),

    url(r'^admin/', include(admin.site.urls)),
]
