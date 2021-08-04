from django.db import models

# Create your models here.
class Todo(models.Model):
  todo=models.TextField(max_length=6000)
  date=models.DateTimeField(auto_now_add=True)
  user=models.CharField(max_length=300)
  def __str__(self):
    return str(self.user) +'ning vazifalari!'