from django.db import models

class Developer(models.Model): 
    name = models.CharField(max_length=250)
    email = models.EmailField() 
    phone = models.CharField(max_length=12)

    def __str__(self): 
        return self.name 