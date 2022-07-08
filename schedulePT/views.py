from django.http import HttpResponse

from django.shortcuts import render, redirect
from .models import StudentInfo


def mainpage(request):
	return render(request, 'index.html')

#CREATE AND READ
def index(request):
	if request.method == "POST":
		studentID = request.POST['studentID']
		name = request.POST['name']
		studentstatus = request.POST['studentstatus']
		professor = request.POST['professor']
		school = request.POST['school']

		StuInfo = StudentInfo(
		studentID = studentID,
		name = name,
		studentstatus = studentstatus,
		professor = professor,
		school = school)

		StuInfo.save()

	else:
		return render(request,'index.html')
	StuInfo =   StudentInfo.objects.all()
	return render(request,'index.html',{'StuInfo':StuInfo})

#UPDATE
def edit(request,sid):
	sid =StudentInfo.objects.get(id = sid)
	StuInfo = StudentInfo.objects.all()
	return render(request,'index.html',{'sid':sid,
		'StuInfo':StuInfo,
		})

def update(request,sid):
	StuInfo = StudentInfo.objects.get(id = sid)
	StuInfo.studentID = request.POST['studentID']
	StuInfo.name = request.POST['name']
	StuInfo.studentstatus = request.POST['studentstatus']
	StuInfo.professor = request.POST['professor']
	StuInfo.school = request.POST['school']
	StuInfo.save()
	return redirect('index')

#DELETE
def delete(request, sid):
   StuInfo = StudentInfo.objects.get(id=sid)
   StuInfo.delete()
   return render(request,'index.html')

#ADDITIONAL PAGE/S
def about(request):
	return render(request, 'about.html')

def Data(request):
	StuInfo =   StudentInfo.objects.all()
	return render(request,'data.html',{'StuInfo':StuInfo})


#__________________________________________________________________________

#from .forms import StudentInfo, UpdateInfo, CreateUserForm
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import authenticate, login, logout
#from django.contrib import messages
#from django.contrib.auth.decorators import login_required


#from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from schedulePT.models import StudentInfo

# """def MainPage(request):
# 	return render(request, 'mainpage.html', {'NameNew': request.POST.get('studentName'), 
# 						'FNameNew': request.POST.get('FstudentName'), 
# 						'LNameNew': request.POST.get('LstudentName'), 
# 						'MNameNew': request.POST.get('MstudentName')})"""

#ito yung unang gawa
#def MainPage(request):
#	if request.method == 'POST':
#		studentName = request.POST['studentName']
#		epstudentName = request.POST['FstudentName']
#		elstudentName = request.POST['LstudentName']
#		emstudentName = request.POST['MstudentName'] 
#
#		StudentInfo.objects.create(studentName=studentName,FstudentName=epstudentName,LstudentName=elstudentName, MstudentName=emstudentName)
#		return redirect('/')
#		
#	infostu = StudentInfo.objects.all()
#	return render(request,'mainpage.html',{'registered':infostu})

#CREATE

# def registration(request):
#     form = StudentInfo()
#     if request.method == 'POST':

#         # form = StudentInfo(request.POST)
#         # if  form.is_valid():
#         #     form.save()
#             return redirect('/')
#     context = {'form':form}
#     return render(request, 'register.html', context)

# #READ

# def list(request):
#     stulist = information.objects.all()
#     context = {'stulist':stulist}
#     return render(request, 'list.html', context)

# def search(request):
#     if request.method == 'GET':
#         search = request.GET.get('search')
#         post = information.objects.all().filter(studentID=search)
#         context = {'post':post}
#         return render(request, 'searchresult.html', context)

# #UPDATE/EDIT

# def UpdateInfo(request, pk):
#     student = information.objects.get(id=pk)
#     form = StudentInfo(instance=student)
#     if request.method == 'POST':
#         # form = StudentInfo(request.POST, instance=student)
#         # if form.is_valid():
#         #     form.save()
#             return redirect('read')
#     context = {'form':form}
#     return render(request, 'register.html', context)

#DELETE

#def delete(request, id):
    #info = information.objects.get(id=id)
   # info.delete()
   # return redirect('/')
