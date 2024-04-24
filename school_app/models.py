from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Batch(models.Model):
    BATCH=(
        ('BCA','BCA'),
        ('BCOM','BCOM'),
        ('BBA','BBA')
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True,null=True)
    name = models.CharField(max_length=100, choices=BATCH, blank=True, null=True)
    year = models.IntegerField()
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True, blank=True)
    

    