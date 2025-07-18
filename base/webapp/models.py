from django.db import models

# Create your models here.



class Snippet(models.Model):
   title     = models.CharField(max_length=200)
   name      = models.CharField(max_length=200)
   roll_no   = models.IntegerField(max_length=200)


   def __str__(self):
      return str(self.title) +'|'+ str(self.name)   

   


