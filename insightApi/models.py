from django.db import models

# Create your models here.
class Tag(models.Model):
  name = models.CharField(max_length=40)
  def __str__(self):
    return self.name

class Card(models.Model):
  texto = models.TextField(max_length=400)
  data_criacao = models.DateTimeField(auto_now_add=True)
  data_modificacao = models.DateTimeField(auto_now=True)
  tags = models.ForeignKey(
    Tag,
    models.SET_NULL,
    blank=True,
    null=True,
  )

  def __str__(self):
    return str(self.pk)


