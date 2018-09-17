from django.db import models

from django.utils import timezone


class Priority(models.Model):
    # The Priority table name that inherits models.Model
    name = models.CharField(max_length=100)  # Like a varchar

    def __str__(self):
        return self.name  # name to be shown when called


class Status(models.Model):
    # The Priority table name that inherits models.Model
    name = models.CharField(max_length=100)  # Like a varchar

    def __str__(self):
        return self.name  # name to be shown when called

class TodoList(models.Model):  # Todolist able name that inherits models.Model
    title = models.CharField(max_length=250)  # a varchar
    content = models.TextField(blank=True)  # a text field
    created = models.DateField(
        default=timezone.now().strftime("%Y-%m-%d"))  # a date
    due_date = models.DateField(
        default=timezone.now().strftime("%Y-%m-%d"))  # a date
    priority = models.ForeignKey(Priority, default="normal")  # a foreignkey
    status = models.ForeignKey(Status, default="pending")

    class Meta:
        ordering = ["-created"]  # ordering by the created field

    def __str__(self):
        return self.title  # name to be shown when called
