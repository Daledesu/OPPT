from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""class StudentInfo(models.Model):
	studentName = models.CharField(max_length=200, null=True)
	FstudentName = models.CharField(max_length=200, null=True)
	LstudentName = models.CharField(max_length=200, null=True)
	MstudentName = models.CharField(max_length=200, null=True)"""

class StudentInfo(models.Model):
	studentID = models.CharField(max_length = 12, unique = True, blank = True)

	name = models.CharField(max_length = 50, blank = True)

	studentstatus = models.CharField(max_length = 50, default = '', blank = True)

	professor = models.CharField(max_length = 50, blank = True)

	school = models.CharField(max_length = 50, blank = True)



# def __str__(self):
#         return self.studentID
