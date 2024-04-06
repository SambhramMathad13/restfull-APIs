from django.db import models
class Studs(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()
    def __name__(self):
        return self.name
    
    