from django.db import models

class PointOfSale(models.Model):
    name = models.CharField(max_length=120, null=False)
    description = models.TextField()
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        