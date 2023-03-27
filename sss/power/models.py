from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    work = models.CharField(max_length=100)
    married = models.BooleanField()
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)

