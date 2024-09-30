from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages

def index(request): 
    all_Person = Person.objects.all()
    return render(request,"index.html", {"all_Person":all_Person})
def about(request):
    return render(request,"about.html")

def form(request):
    if request.method =="POST":
        name = request.POST["name"]
        age = request.POST["age"]
        person = Person.objects.create(
            name=name,
            age=age
        )
        person.save()
        messages.success(request, "บันทึกข้อมูลสำเร็จ")
        return redirect("/")
    else:
        return render(request,"form.html")

def delete(request,Person_id):
    person = Person.objects.get(id=Person_id)
    person.delete()
    messages.success(request,"ลบข้อมูลเรียบร้อย")
    return redirect("/")

def edit(request, Person_id):
    person=Person.objects.get(id=Person_id)
    return render(request, 'edit.html',{'person':person})
