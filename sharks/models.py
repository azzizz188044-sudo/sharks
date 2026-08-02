from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='teachers/')
    description = models.TextField()

    def __str__(self):
        return self.name

class Result(models.Model):
    image = models.ImageField(upload_to='results/')

    def __str__(self):
        return f"Result {self.id}"
