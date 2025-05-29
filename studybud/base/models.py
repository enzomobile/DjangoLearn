from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants =
    updated = models.DateTimeField(auto_now=True) # Will update
    created = models.DateTimeField(auto_now_add=True) # Will never change

    def __str__(self):
        return self.name