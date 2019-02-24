from django.db import models
import datetime

description_empty='description was not added yet, be the first who add it!'

class Band(models.Model):
    name = models.CharField(default='<unknown name>',max_length=50)
    description = models.CharField(default=description_empty,max_length=5000)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.name == other.name and self.id == other.id


class Album(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField(default=datetime.date.today)
    num_stars = models.IntegerField(default=0)
    description = models.CharField(default=description_empty,max_length=5000)
    band=models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.name == other.name and self.band == other.band and self.id == other.id

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(default='<unknown name>',max_length=50)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.name == other.name and self.album == other.album and self.id == other.id
