from django.db import models

# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Row(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

class Column(models.Model):
    row = models.ForeignKey(Row, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    def __str__(self):
        return self.name
