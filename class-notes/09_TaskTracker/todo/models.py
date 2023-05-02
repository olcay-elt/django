from django.db import models

# Create your models here.
class Todo(models.Model):
    PRIORITY=(
        (1,'High'),
        (2,'Medium'),
        (3,'Low')
    )
    task=models.CharField(max_length=50)
    description=models.TextField()
    is_done=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    priority=models.IntegerField(choices=PRIORITY,default=2)

    def __str__(self):
        return self.task