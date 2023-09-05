from django.db import models
from datetime import datetime



# Create your models here.
 
class wings(models.Model):
    
    add=models.TextField()
    point=models.TextField()
    description=models.TextField()
    date=models.TextField(null="True")
    
    def _str_(self):
        return self.add

        

    
    