from django.db import models



class Music(models.Model):

    artiste         =models.CharField(max_length=100)




    def __str__(self):
        return self.artiste
