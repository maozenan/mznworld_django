from django.db import models
# from __future__ import unicode_literals

class Book(models.Model):
    username = models.CharField(max_length=18,default='')
    password = models.CharField(max_length=18,default='')

    def __unicode__(self):
        return self.username,self.password