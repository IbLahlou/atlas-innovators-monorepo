from django.db import models
from .person import Person

class Parent(Person):
    child_id = models.JSONField(null=True, blank=True)
