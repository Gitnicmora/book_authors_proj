from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.title} {self.description}'


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(default="")
    books = models.ManyToManyField(Book, related_name='authors')

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
