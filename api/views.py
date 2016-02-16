#from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListCreateAPIView, ListAPIView, GenericAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView 
from .models import PeoplePhone
from .serializers import PhoneSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response



    
class LookupPhoneView(GenericAPIView):
    serializer_class = PhoneSerializer
    
    def get_queryset(self):
        queryset = PeoplePhone.objects.all()
        mobile_phone = self.request.query_params.get('mobile_phone', None)
        queryset = queryset.filter(mobile_phone=mobile_phone)
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

    
    