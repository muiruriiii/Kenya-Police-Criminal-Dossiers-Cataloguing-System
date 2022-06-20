from django.db import models

class CrimeInsert(models.Model):
	 description=models.CharField(max_length=400)
	 crimeNature=models.CharField(max_length=100)
	 class Meta:
	 	db_table="tbl_crime"

class InsertUser(models.Model):
	 fName=models.CharField(max_length=100)
	 lName=models.CharField(max_length=100)
	 email=models.CharField(max_length=100)
	 tel=models.CharField(max_length=100)
	 password=models.CharField(max_length=400)
	 nationalID=models.CharField(max_length=100)
	 gender=models.CharField(max_length=100)
	 address=models.CharField(max_length=100)
	 class Meta:
	 	db_table="tbl_citizen"
