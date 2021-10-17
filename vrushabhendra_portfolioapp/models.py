from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(primary_key=True)
    comment = models.TextField(max_length=600)

    def __str__(self) -> str:
        return self.name
