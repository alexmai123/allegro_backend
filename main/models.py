from django.db import models
from enum import Enum as En

class Enum(En):
    @classmethod
    def to_choices(cls):
        return ((member.value, member.name) for member in cls)

    @classmethod
    def parse(cls, name):
        return cls.__members__[name]


class Role(models.Model):
    name = models.TextField(null=False)
    staging = models.BooleanField(default=True)

class Member(models.Model):
    class Year(Enum):
        YEAR_1 = 'Year 1'
        YEAR_2 = 'Year 2'
        YEAR_3 = 'Year 3'
        YEAR_4 = 'Year 4'
        GRADUATED = 'Graduated'
        MASTER = 'Master'
        OTHER = 'Other'

    class Section(Enum):
        ALTO = 'Alto'
        BASS = 'Bass'
        SOPRANO = 'Soprano'
        TENOR = 'Tenor'
        OTHER = 'Other'

    name = models.TextField(null=False)
    description = models.TextField(null=False, blank=True, default='')
    pro_pic = models.TextField(null=True)
    active = models.BooleanField(default=True)
    email = models.CharField(null=True, max_length=255)
    phone = models.TextField(null=True, max_length=20)
    year = models.CharField(choices=Year.to_choices(), default=Year.OTHER.value, max_length=16)
    section = models.CharField(choices=Section.to_choices(), default=Section.OTHER.value, max_length=16)
    roles = models.ManyToManyField(to=Role)
    staging = models.BooleanField(default=True)


class Event(models.Model):
    title = models.TextField()
    description = models.TextField()
    picture = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    staging = models.BooleanField(default=True)

