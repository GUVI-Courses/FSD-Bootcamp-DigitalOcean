from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Contact,Order,Employee


# Create your views here.
def index(request):
    return render(request,'index.html')

def products(request):
    return render(request,'products.html')

def services(request):
    return render(request,'services.html')

def handlelogin(request):
      if request.method == 'POST':
        # get parameters
        loginusername=request.POST['email']
        loginpassword=request.POST['pass1']
        user=authenticate(username=loginusername,password=loginpassword)
       
        if user is not None:
            login(request,user)
            messages.info(request,"Successfully Logged In!")
            return redirect('/register')

        else:
            messages.error(request,"Invalid Credentials. Please try again.")
            return redirect('/login')             
      return render(request,'login.html')         

def signup(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1 != pass2:

            messages.error(request,"Password do not Match, Please Try Again!")
            return redirect('/signup')
        try:
            if User.objects.get(username=email):
                messages.warning(request,"Email Already Exists")
                return redirect('/signup')
        except Exception as identifier:            
            pass 
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email Already Exists")
                return redirect('/signup')
        except Exception as identifier:
            pass        
        # checks for error inputs
        user=User.objects.create_user(email,email,pass1)
        user.save()
        messages.info(request,'Thank you for Signing Up')
        # messages.info(request,"Signup Successful Please Login")
        return redirect('/login')    
    return render(request,"signup.html")        

def contact(request):
    if not request.user.is_authenticated:        
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')    
    if request.method=="POST":          
        name = request.POST.get('name')
        email = request.POST.get('email')
        num = request.POST.get('num')
        desc = request.POST.get('desc')
        query= Contact(name=name,email=email,number=num,message=desc)
        query.save()
        messages.info(request,"Submitted Successfully")
        return render(request,'contact.html')  
  
    return render(request,'contact.html')      
    


def register(request):
    if not request.user.is_authenticated:        
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    trainer=Employee.objects.all()
    context={"trainer":trainer}      
    if request.method == 'POST':

        # get parameters
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender'] 
        locality=request.POST['locality']
        phone=request.POST['phone']
        slot=request.POST['slot']
        trainer=request.POST['trainer']
        order=Order(name=name,email=email,age=age,gender=gender,locality=locality,phone=phone,slot=slot,trainer=trainer)
        order.save()    
        messages.success(request,"Registration Successful")
        return redirect('/')
    return render(request,'join.html',context=context)



def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Successful")
    return redirect('/login')