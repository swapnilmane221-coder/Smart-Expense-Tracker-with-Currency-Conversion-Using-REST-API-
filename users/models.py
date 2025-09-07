from django.db import models

# Create your models here.nd 🌟  *************/

class expense(models.Model):
     id=models.AutoField(primary_key=True)
     title = models.CharField(max_length=100)
     category = models.CharField(max_length=100)
     amount = models.FloatField()
     description = models.TextField()
     date = models.DateField()

     def __str__(self):
          return self.title   
     
