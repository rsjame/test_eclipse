from django.db import models

class Eploee(models.Model):
    name=models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name