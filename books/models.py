from django.db import models


# Create your models here.

class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish = models.CharField(max_length=32)
    pub_date = models.DateTimeField()
    objects = models.Manager()

    def __str__(self):
        return self.title
