from django.db import models
from django.utils.text import slugify

# Create your models here.
class Table(models.Model):
    name = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.name

class Row(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="rows")

class Column(models.Model):
    row = models.ForeignKey(Row, on_delete=models.CASCADE, related_name="columns")
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    def __str__(self):
        return self.name
