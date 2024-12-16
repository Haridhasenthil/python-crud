from django.db import models

# Create your models here.
from mongoengine import Document, fields

class Person(Document):
    first_name = fields.StringField(required =True)
    last_name = fields.StringField(required =True)
    # meta = {
    #     'db_alias':'person'
    # }
    # def __init__ (self,first_name,last_name):
    #     self.first_name=first_name
    #     self.last_name=last_name
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)

