from django.shortcuts import render
from app1.models import Studyhall,Expense,Enquiry,Course,Student

def funs(request):
	studyhalls = Studyhall.objects.all()
	expenses=Expense.objects.all()
	enquiries=Enquiry.objects.all()
	return render(request,"app1/index.html",{
		"studyhalls":studyhalls,
		"expenses":expenses,
		"enquiries":enquiries})
	
	# return render(request,"app1/index.html")
# Create your views here.

def view_studyhalls(request):
	studyhalls=Studyhall.objects.all()
	return render(request,"app1/index.html",{"studyhalls":studyhalls})
	expenses=Expense.objects.all()
	return render(request,"app1/index.html",{"expenses":expenses})
	enquiries=Enquiry.objects.all()
	return render(request,"app1/index.html",{"enquiries":enquiries})

