'''
Created on Feb 15, 2016

@author: mariah
'''

from rest_framework import serializers
from .models import PeoplePhone


class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PeoplePhone
        fields = ('id','url','name', 'mobile_phone')
        
