from django.shortcuts import render
from .models import *

# Create your views here.
def registerpage(request):
    return render(request,"app/register.html")

#view for user registration
def userregister(request):
    if request.method=='POST':
        firstname=request.POST['Fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        Cpassword=request.POST['cpassword']

        #we will cheak user already exist or not
        usser=user.objects.filter(Email=email)

        if usser:
            message="user already exist"
            return render(request,"app/register.html",{'msg':message})
        else:
            if password==Cpassword:
                newuser=user.objects.create(Firstname=firstname,Lastname=lastname,Email=email,Contact=contact,Password=password)  
                message="user register sucssefully" 
                return render(request,"app/login.html",{'msg':message})
            else:
                message="password and confirm password does not match"
                return render(request,"app/register.html",{'msg':message})

#login view
def loginpage(request):
    return render(request,"app/login.html")


def loginuser(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        #cheak emailid with database
        usser=user.objects.get(Email=email)

        if usser:
            if usser.Password==password:
                #we getting user data to session
                request.session['Firstname']=usser.Firstname
                request.session['Lastname']=usser.Lastname
                request.session['Email']=usser.Email
                return render(request,"app/home.html")
            else:
                message="password does not match"
                return render(request,"app/login.html",{'msg':message})


        else:
            message='user does not exist'
            return render(request,"app/register.html",{'msg':message})
