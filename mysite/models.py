from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateTimeField()

    def __str__(self):
        return self.name
    

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='speakers/')

    def __str__(self):
        return self.name

# Create your models here.
