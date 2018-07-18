from django.db import models

class Studyhall(models.Model):
	name = models.CharField(max_length=50)
	area = models.CharField(max_length=250)
	def __str__(self):
		return("%s %s"%(self.name,self.area))
	class Meta:
		db_table="app1_studyhall"

class Expense(models.Model):
	studyhall=models.ForeignKey(Studyhall,on_delete = None)
	date=models.DateField()
	name = models.CharField(max_length=250)
	desc=models.TextField(max_length=250)
	value=models.IntegerField()

	def __str__(self):
		return("%s,%s,%s,%s,%s"%(self.studyhall,self.date,self.name,self.desc,self.value))

class Course(models.Model):
	name=models.CharField(max_length=250)
	def __str__(self):
		return(self.name)

class Student(models.Model):
	name = models.CharField(max_length=250)
	address = models.TextField(max_length=250)
	phone = models.CharField(max_length=250)
	email = models.CharField(max_length=250)

class Enquiry(models.Model):
	name = models.CharField(max_length=250)
	course=models.ForeignKey(Course,on_delete = None)
	student=models.ForeignKey(Student,on_delete = None)

	def __str__(self):
		return("%s %s %s"%(self.name,self.course,self.student))