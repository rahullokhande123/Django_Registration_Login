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
            if password1==password:
                data={
                    'name1':name1,
                    'email1':email1,
                    'contact1':contact1,
                    'password1':password1
                }
                return render(request,'deshbord.html',data)
            else:
                msg="email and password not match"
                return render(request,'login.html',{'msg':msg}) 
        else:
            msg='email id not registerd'
        return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')

def registerdata(request):
    print(request.method)
    print(request.POST)

    cstoken=request.POST.get('csrfmiddlewaretoken')
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    password=request.POST.get('password')


 

        