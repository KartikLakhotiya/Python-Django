from django.shortcuts import render
from .models import CourseName
# Create your views here.
# def index(request):
#     context={'name':'kartik'}
#     return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def contact(request):
    return render(request,'contact.html')

# def add(request):
#     if request.method == 'POST':
#         principle = int(request.POST['principle'])
#         rate = int(request.POST['rate'])
#         num = int(request.POST['numy'])
#         result = principle * rate * num / 100
#         return render(request,'result.html',{'result':result})
    
def course_details(request):
    return render(request,'course_details.html')

def courses(request):
    
    return render(request,'courses.html')

def events(request):
    return render(request,'events.html')

def index(request):
    courseobj = CourseName.objects.all()
    context = {'courseobj':courseobj}
    return render(request,'index.html',context)

def pricing(request):
    return render(request,'pricing.html')

def trainers(request):
    return render(request,'trainers.html')