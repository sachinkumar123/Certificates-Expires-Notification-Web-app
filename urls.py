from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^feaspot/', include('feaspot.urls')),
    url(r'^admin/', admin.site.urls),
]
