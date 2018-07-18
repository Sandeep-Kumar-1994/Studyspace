from django.shortcuts import render
from app1.models import Studyhall,Expense,Enquiry,Course,Student

def funs(request):
	if request.method=="POST":
		data=request.POST
		if data.get("enquiry"):
			course_inst = Course.objects.get(pk=data.get("enq_course"))
			stdudent_inst = Student.objects.get(pk=data.get("enq_student"))
			enq=Enquiry(
				name=data.get("enq_name"),
				student=stdudent_inst,
				course=course_inst
				)
			enq.save()
		elif data.get("expense"):
			studyhall_inst=Studyhall.objects.get(pk=data.get("exp_studyhall"))
			exp=Expense(
				studyhall=studyhall_inst,
				date=data.get("exp_date"),
				name=data.get("exp_name"),
				desc=data.get("exp_desc"),
				value=data.get("exp_value"),
				)
			exp.save()
		else:
			hall=Studyhall(name=data.get("hall_name"),
				area=data.get("hall_area"))
			hall.save()

	studyhalls = Studyhall.objects.all()
	expenses=Expense.objects.all()
	enquiries=Enquiry.objects.all()
	courses=Course.objects.all()
	students=Student.objects.all()
	return render(request,"app1/index.html",{
		"studyhalls":studyhalls,
		"expenses":expenses,
		"enquiries":enquiries,
		"students":students,
		"courses":courses		
		})
	
	# return render(request,"app1/index.html")
# Create your views here.

def view_studyhalls(request):
	studyhalls=Studyhall.objects.all()
	return render(request,"app1/index.html",{"studyhalls":studyhalls})
	

