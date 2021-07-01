from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Salesman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, null=False)
    second_name = models.CharField(max_length=120, null=False)

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created',False):
        Salesman.objects.get_or_create(user=instance)
        print("se creo un salesman para el usuario  recien creado")
