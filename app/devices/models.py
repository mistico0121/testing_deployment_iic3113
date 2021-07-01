from django.db import models
from django.urls import reverse

class Device(models.Model):
    name = models.CharField(max_length=120, null=False)
    model_number = models.CharField(max_length=120, null=False)
    brand = models.CharField(max_length=120, null=False)
    os = models.CharField(max_length=120, null=False)
    color = models.CharField(max_length=120, null=False)
    memory = models.PositiveIntegerField()
    internal_memory = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    sale = models.FloatField()
    point_of_sale = models.ForeignKey('point_of_sales.PointOfSale', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("device-show", kwargs={"id": self.id})

    def __str__(self):
        return self.name