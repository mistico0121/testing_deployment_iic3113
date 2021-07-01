from django.db import models
from django.urls import reverse

class AttendanceTablet(models.Model):
    name = models.CharField(max_length=120, null=False)
    online = models.BooleanField(default=False, null=False)
    point_of_sale = models.ForeignKey('point_of_sales.PointOfSale', on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse("attendance_tablet-show", kwargs={"id": self.id})

    def __str__(self):
        return self.name