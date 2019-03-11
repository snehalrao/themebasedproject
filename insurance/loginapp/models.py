from django.db import models

# Create your models here.

class  User_insurance(models.Model):
    usr_id = models.CharField(max_length = 100, unique = True)
    usr_pass = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.usr_id
