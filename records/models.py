import json

from django.db import models


class OB(models.Model):
    citizenID = models.IntegerField()
    crimeID = models.IntegerField()
    obNo = models.CharField(max_length=30)
    reportDate = models.DateTimeField()
    actionTaken = models.CharField(max_length=200)
    file = models.JSONField()
    officerID = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)
    hasCase = models.IntegerField(default=0)

    class Meta:
        db_table = "tbl_ob"


class Case(models.Model):
    officerID = models.IntegerField()
    caseNumber = models.CharField(max_length=40)
    caseStatus = models.CharField(max_length=20)
    obID = models.IntegerField()
    generateDate = models.DateTimeField(auto_now_add=True)
    previousStation = models.IntegerField()
    currentStation = models.IntegerField()

    class Meta:
        db_table = "tbl_case"


class PoliceStation(models.Model):
    location = models.CharField(max_length=100)
    officersCount = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    ocsID = models.IntegerField()
    stationNumber = models.CharField(max_length=100)
    stationStatus = models.BooleanField(default=False)
    establishDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_station'


class Evidence(models.Model):
    description = models.CharField(max_length=400)
    evidenceFiles = models.ImageField()
    Form=models.ImageField()

    class Meta:
        db_table = "tbl_evidence"


class CrimeList(models.Model):
    crimeID = models.AutoField(auto_created=True, primary_key=True)
    crimeName = models.TextField(max_length=400)

    class Meta:
        db_table = "tbl_crimelist"


class Crime(models.Model):
    description = models.CharField(max_length=400)
    crimeID = models.IntegerField()
    citizenID = models.IntegerField(default=0)
    reportTime = models.DateTimeField(auto_now_add=True)
    hasOB = models.IntegerField()

    class Meta:
        db_table = "tbl_crime_report"


class CrimeAnonymous(models.Model):
    description = models.CharField(max_length=400)
    crimeID = models.IntegerField()
    citizenID = models.IntegerField(default=0)
    reportTime = models.DateTimeField(auto_now_add=True)
    hasOB = models.BooleanField(default=False)

    class Meta:
        db_table = "tbl_crime_report"


class CrimeAnonymous(models.Model):
    description = models.CharField(max_length=400)
    crimeID = models.IntegerField()
    reportTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tbl_crime_report_anonymous"


class Citizen(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    password = models.CharField(max_length=400)
    nationalID = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    citizenImage = models.ImageField()
    joinDate = models.DateTimeField(auto_now=True)
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
    stationID = models.IntegerField()

    class Meta:
        db_table = "tbl_police_officer"
