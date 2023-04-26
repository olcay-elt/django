from django.db import models

# Create your models here.
class Student(models.Model):
    number=models.IntegerField()
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=30)
    about=models.TextField(blank=True,null=True)
    email=models.EmailField(blank=True)
    is_active=models.BooleanField(default=True)
    ragister_date=models.DateField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)    # her update de günceller
    avatar=models.ImageField(blank=True,null=True) #pillow kur, settings ve url de istenen güncellemeleri yap
                             
    def __str__(self):
        return f"{self.first_name}-{self.last_name}"
    
    
        # ordering=('number')
        ordering=('-number',)
        verbose_name='Ogrenci'
        verbose_name_plural='ogrenciler'




