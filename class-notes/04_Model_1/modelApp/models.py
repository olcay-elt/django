from django.db import models

# Create your models here.
class Student(models.Model):
    number=models.IntegerField()
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=40)
    about=models.TextField(blank=True,null=True)
    register_date=models.DateTimeField(auto_now_add=True,null=True) # ilk kayıt tarihi
    update_date=models.DateTimeField(auto_now=True,null=True) # güncelleme tarihi

    def __str__(self):
        # return self.first_name
        return  f"{self.first_name} {self.last_name}" 
    
    class Meta:
        ordering=["first_name"]
        verbose_name="Student Table"
