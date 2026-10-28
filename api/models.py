from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

