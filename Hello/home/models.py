from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    desc = models.TextField(max_length=1000)
    phone = models.CharField(max_length=12)
    date = models.DateField()

    def __str__(self):
        return self.name
