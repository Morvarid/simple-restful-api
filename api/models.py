from django.db import models


class PeoplePhone(models.Model):  
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=13)
    
    #def get_absolute_url(self):
        #return reverse("flavors:detail", kwargs={"phone_number": self.phone_number})
    