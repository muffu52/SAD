from django.db import models

class Counter(models.Model):
    name = models.CharField(max_length=10)
    value = models.IntegerField()

    # def __str__(self):
    #         return f"{self.id} {self.name} {self.value}"
