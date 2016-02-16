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
#     url(
#         regex=r"^who/people(?P<pbone_number>[-\w]+)/$",
#         view=views.LookUpReadUpdateDeleteView.as_view(),
#         name="phone_rest_api"
#     ),
#     url(
#         regex=r"^who/(?P<mobile_phone>[-\w]+)/$",
#         view=views.LookupPhoneView.as_view(),
#         name="phone_query_api"
#     ),   
#      url(
#         regex=r"^who/(?P<pk>\d+)/$",
#         view=views.LookUpReadUpdateDeleteView.as_view(),
#         name="phone_rest_api"
#     ),     
    
   
] + router.urls

