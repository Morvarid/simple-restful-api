from django.conf.urls import url

from api import views
from rest_framework import routers
from api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'people', UserViewSet)

urlpatterns = [
    url(
        regex=r"^who/$",
        view=views.LookupPhoneView.as_view(),
        name="phone_rest_api_list"
    ),

   
] + router.urls

