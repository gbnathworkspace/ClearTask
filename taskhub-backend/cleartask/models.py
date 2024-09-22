
from django.db import models

class TestEntry(models.Model):
    id = models.IntegerField(primary_key=True)  # Explicitly define the primary key
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name