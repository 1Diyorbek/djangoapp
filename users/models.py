from django.db import models


class Address(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Role(models.TextChoices):
    bachelor = ('b', 'Bakalavr')
    master = ('m', 'Magistr')
    phd = ('d', 'phd')


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=Role.choices, default=Role.bachelor)
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="student")

    def __str__(self):
        return self.first_name
