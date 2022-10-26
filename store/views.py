import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models import books, user

# Create your views here.


def home(request):
    items = books.objects.all()
    param={'items':items}
    return render(request, 'store.html', param)

def register(request):
    name = request.POST.get('name','')
    email = request.POST.get('email','')
    dob = request.POST.get('dob','')
    phone = request.POST.get('phone','')
    password = request.POST.get('password','')
    msg=''
    if(name!='' and email!='' and dob!='' and phone!='' and password!=''):
        register = user(name=name, email=email, dob=dob, contact=phone, password=password)
        register.save()
        msg="You have successfully registered"
    param = {'msg':msg}
    return render(request, 'register.html')

def login(request):
    name = request.POST.get('name','')
    password = request.POST.get('password','')
    msg = ''
    try:
        loggedin = request.session['loggedin']
    except:
        loggedin = False
    if loggedin:
        return redirect('home')
    if(name!='' and password!=''):
        id = user.objects.filter(name=name)
        if(id):
            if(id[0].password==password):
                request.session['loggedin']=True
                return redirect('home')
            else:
                msg='Incorrect Password'
        else:
            msg="Username Does not exists"
    param = {'name': name, 'password': password, 'msg': msg}
    return render(request, 'login.html', param)
