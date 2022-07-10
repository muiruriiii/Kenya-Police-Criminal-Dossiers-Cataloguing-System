import json

from django.db import models


class Crime(models.Model):
    description = models.CharField(max_length=400)
    crimeNature = models.CharField(max_length=100)
    class Meta:
        db_table = "tbl_crime"


class Citizen(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    password = models.CharField(max_length=400)
    nationalID = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "tbl_citizen"


class Criminal(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    nationalID = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    crimeID = models.CharField(max_length=100)
    criminalStatus = models.CharField(max_length=100)
    locationArrested = models.CharField(max_length=100)
    arrestDate = models.DateTimeField(max_length=100)

    class Meta:
        db_table = "tbl_criminal"


class Officer(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    nationalID = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    password = models.CharField(max_length=400)
    employmentStatus = models.BooleanField(default=False)
    employmentDate = models.DateTimeField()

    class Meta:
        db_table = "tbl_police_officer"

