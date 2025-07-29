from django.db import models

# Create your models here.


class AppUser(models.Model):
    name = models.CharField(max_length=52, null=False, default="Name")

    def __str__(self):
        return f"{self.name}"