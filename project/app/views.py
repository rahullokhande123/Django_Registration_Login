from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def registerdata(request):
    print(request.method)
    print(request.POST)

    cstoken=request.POST.get('csrfmiddlewaretoken')
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    password=request.POST.get('password')

   