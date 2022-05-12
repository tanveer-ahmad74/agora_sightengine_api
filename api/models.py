from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(blank=True)
    isCompleted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title

