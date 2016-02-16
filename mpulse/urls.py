from django.conf.urls import include, url
from django.contrib import admin
from api import views

urlpatterns = [

    url(r'^api/', include('api.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]

