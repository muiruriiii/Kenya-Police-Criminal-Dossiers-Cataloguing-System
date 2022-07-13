import json

from django.db import models



# class OB(models.Model):
#     file = models.FileField(max_length=400)
#
#     class Meta:
#         db_table = "tbl_ob"

class CrimeList(models.Model):
    crimeName = models.TextField(max_length=400)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tbl_crimelist"

class Crime(models.Model):
    description = models.CharField(max_length=400)
    crimeID = models.ForeignKey(CrimeList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tbl_crimereport"


class Citizen(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    password = models.CharField(max_length=400)
    nationalID = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    joinDate = models.DateTimeField()
    accountStatus = models.BooleanField(default=False)

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
    arrestDate = models.DateTimeField()

    class Meta:
        db_table = "tbl_criminal"


class Officer(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    nationalID = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    password = models.CharField(max_length=400)
    employmentStatus = models.BooleanField(default=False)
    employmentDate = models.DateTimeField()

    class Meta:
        db_table = "tbl_police_officer"

