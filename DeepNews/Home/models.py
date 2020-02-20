from mongoengine import *
from django.contrib.postgres.fields import ArrayField

connect('deepnews')


class bbc(DynamicDocument):
    link=StringField()
    headline=StringField()
    content=ArrayField(ArrayField(StringField()))
    date=DateField()
    image=StringField()
    magnitude=FloatField()
    score=FloatField()
class cnn(DynamicDocument):
    link=StringField()
    headline=StringField()
    content=ArrayField(ArrayField(StringField()))
    date=DateField()
    image=StringField()
    magnitude=FloatField()
    score=FloatField()
class sky(DynamicDocument):
    link=StringField()
    headline=StringField()
    content=ArrayField(ArrayField(StringField()))
    date=DateField()
    image=StringField()
    magnitude=FloatField()
    score=FloatField()
class article(DynamicDocument):
    link=StringField()
    headline=StringField()
    content=ArrayField(ArrayField(StringField()))
    date=DateField()
    image=StringField()
    magnitude=FloatField()
    score=FloatField()
