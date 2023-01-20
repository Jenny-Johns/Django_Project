from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def index(request):
    data=Student.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        course=request.POST.get('course')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        print(name,course,email,phone,gender)
        query=Student(name=name,course=course,email=email,phone=phone,gender=gender)
        query.save()
    return render(request,"index.html")

def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        course=request.POST['course']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        print(name,course,email,phone,gender)
        query=Student(name=name,course=course,email=email,phone=phone,gender=gender)
        query.save()
        return redirect("/")
    
    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)


def deleteData(request,id):
    data=Student.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)

        
def about(request):
    return render(request,"about.html")