from django.db import models

# Create your models here.
class Thread(models.Model):
	title = models.CharField(max_length = 120)
	text = models.TextField(blank = True, null = True)
	username = models.CharField(max_length = 120)
	createdAt = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title