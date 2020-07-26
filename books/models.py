from django.db import models


# Create your models here.
class Author(models.Model):
    gender_choices = {
        ('male', '男'),
        ('female', '女'),
    }
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(choices=gender_choices, max_length=16)
    address = models.CharField(max_length=64)
    authorDetail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    telephone = models.BigIntegerField()
    address = models.CharField(max_length=128)
    birthday = models.DateTimeField()


class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    email = models.EmailField()


class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish = models.ForeignKey(to='Publish', to_field='nid', on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField()
    authors = models.ManyToManyField(to="Author")
    objects = models.Manager()

    def __str__(self):
        return self.title
