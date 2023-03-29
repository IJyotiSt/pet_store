from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
def about_page(request):
    context = {
        "title":"About Page",
        "content":" Welcome to the about page."
    }
    return render(request, "base/about_page.html", context)

def service_page(request):
    context = {
        "title":"service Page",
        "content":" Welcome to the service page."
    }
    return render(request, "base/service_page.html", context)

def register_page(request):
    form=RegisterForm()
    context = {
        "title":"Registration Page",
        "form":form
    }

    if request.method=='POST':
          form=RegisterForm(request.POST)
          context = {
        "title":"Registration Page",
        "form":form
    }

          if form.is_valid():
          
            user=form.save(commit=True)
            user.set_password(user.password)
            user.save()
            return redirect('/login')
          else:
              return render(request, "base/register.html", context)
    return render(request, "base/register.html", context)

def login_page(request):
    loginform=AuthenticationForm()
    if request.method=='POST':
        username=request.POST.get('username')
        pwd=request.POST.get('password')
        print(username,pwd)
        user=authenticate(username=username,password=pwd)
        print(user)
        if user!=None:
            login(request,user)
            print(request,user)
            return redirect('/')
        else:
            msg='Invalid username or password'
            return render(request,'base/login.html',{'form':loginform,'msg':msg})
        
    return render(request,'base/login.html',{'form':loginform})

def logOut(request):
    print(request.user)
    logout(request)
    print(request.user)
    return redirect('/')