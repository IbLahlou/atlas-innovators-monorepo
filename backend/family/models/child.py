from django.db import models
from .person import Person

class Child(Person):
    score = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    parent_id = models.JSONField(null=True, blank=True)
