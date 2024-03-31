from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    author = models.CharField(max_length=40)
    price = models.FloatField()

    def __str__(self):
        return f"""
        Title -> {self.title}
        description -> {self.description}
        author -> {self.author}
        price -> {self.price}"""
