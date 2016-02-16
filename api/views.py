#from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListCreateAPIView, ListAPIView, GenericAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView 
from .models import PeoplePhone
from .serializers import PhoneSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response





# class LookUpCreateReadView(ListCreateAPIView):
# 
#     queryset = PeoplePhone.objects.all() 
#     serializer_class = PhoneSerializer
#     lookup_field = 'phone_number'
    
# class LookUpReadUpdateDeleteView(RetrieveUpdateDestroyAPIView): 
#     queryset = PeoplePhone.objects.all()
#     serializer_class = PhoneSerializer
#     lookup_field = 'phone_number'
    
class LookupPhoneView(GenericAPIView):
    serializer_class = PhoneSerializer
    
    def get_queryset(self):
        queryset = PeoplePhone.objects.all()
        mobile_phone = self.request.query_params.get('mobile_phone', None)
        queryset = queryset.filter(phone_number=mobile_phone)
        return queryset
    
    def get(self, request):
        queryset = self.get_queryset()
        serializer = PhoneSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PeoplePhone.objects.all()
    serializer_class = PhoneSerializer
    
    
'''class UserCountView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        user_count = User.objects.filter(active=True).count()
        content = {'user_count': user_count}
        return Response(content)'''
    
    
    
    