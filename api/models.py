from django.db import models


class PeoplePhone(models.Model):  
    name = models.CharField(max_length=150)
    mobile_phone = models.CharField(max_length=13)
