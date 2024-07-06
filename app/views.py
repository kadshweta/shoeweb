from django.shortcuts import render,redirect
from .models import Student


def index(request):
    print("Rendering index.html")
    if request.method =='POST':
       
        # retrive the data from user
        uname=request.POST.get("user")
        passw=request.POST.get("password")
        print(uname,passw)
        
        data=Student(username=uname,password=passw)
    
        data.save()
        print("done")
    #     # create an object for models 
    

    return render(request,'app/index.html')