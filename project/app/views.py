from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        data={
            'name':name,
            'email':email,
            'contact':contact,
            'password':password
        }
        request.session['data']=data
        return render(request,'login.html')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST': 
        data1=request.session.get('data')
        print(data1)
        email=request.POST.get('email','guest')
        password=request.POST['password']
        print(email)
        if data1== None:
            msg = "Session Not Register Please Register First"
            return render(request,'login.html',{"msg":msg})
        elif email == data1['email']:
            if data1['password']==password:
                my_data={
                    'nm':data1['name'],
                    'em':data1['email'],
                    'con':data1['contact'],
                    'pas':data1['password']
                }
                return render(request,'deshbord.html',my_data)
            else:
                msg="Password is inccorrect"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Email is incorrect"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')

def logout(request):
    if request.session:
        request.session.flush()
        return render(request,'home.html')

 

   

        