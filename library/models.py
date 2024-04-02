from django.db import models
from users.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birt_date = models.DateField(auto_created=True)

    def __str__(self):
        return self.first_name


class Book(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    price = models.FloatField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"""title = > {self.title}  price => {self.price}"""


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class BookingBook(models.Model):
    user = models.ManyToManyField(User)
    book = models.ManyToManyField(Book)
    take_date = models.DateTimeField(auto_now_add=True)
    returned_book = models.BooleanField(default=False)

    def __str__(self):
        if self.returned_book:
            return "Qaytarilgan"
        else:
            return "Qaytarilmagan"
