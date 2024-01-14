from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Author, Book


def hello_world(request):
    return HttpResponse("Hello, World!")
def mercedes(request):
    return HttpResponse("Hello Lewis")
def mercedes(request):
    return HttpResponse("Hello Lewis")
def current_datetime(request):
    now = datetime.now()
    return render(request, 'hello_app\\current_datetime.html', {'now': now})


def time_after_10_hours(request, hours):
    try:
        hours = int(hours)
    except ValueError:
        return HttpResponse("Invalid input. Please provide a valid integer.")

    current_time = datetime.now()
    time_after_10_hours = current_time + timedelta(hours=hours)

    return HttpResponse(f"Current Time: {current_time}<br>Time After {hours} Hours: {time_after_10_hours}")
from django.shortcuts import render

def hello(request):
    context = {
        'name': 'Kushal',
        'age': 23,
    }
    return render(request, 'hello_app/hello.html', context)

from django.shortcuts import render
from .models import Book

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'hello_app/author_list.html', {'authors': authors})

from django.shortcuts import render, redirect  
from .forms import EmployeeForm  
from .models import Employee  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'hello_app/index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"hello_app/show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'hello_app/edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'hello_app/edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  





