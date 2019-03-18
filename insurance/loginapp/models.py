from django.db import models

# Create your models here.

class  Login_details(models.Model):
    usr_id = models.CharField(max_length = 10,unique = True)
    usr_pass = models.CharField(max_length = 10,unique = True)

    def __str__(self):
        return usr_id
