from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}  / Is Done: {self.is_done}'

    class Meta:
        db_table = 'todos'
