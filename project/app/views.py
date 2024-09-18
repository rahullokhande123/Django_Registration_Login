from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        # print(email,password)
        name1=request.COOKIES['name']
        email1=request.COOKIES['email']
        contact1=request.COOKIES['contact']
        password1=request.COOKIES['password']
        # print(name,email,contact,password)
        if email1==email:
           
        else:
            msg='email id not registerd'
        return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')

def registerdata(request):
    print(request.method)
    print(request.POST)

  


 

        