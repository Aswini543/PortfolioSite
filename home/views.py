from django.shortcuts import render,HttpResponse

from home.models import Contact


# Create your views here.

def home(request):
    context={'name':"aswini",'company':"stockone"}
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html')
    
def projects(request):
    return render(request,'projects.html')
    
def contact(request):
    if(request.method=='POST'):
        # print("This is post")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(name,email,phone,desc)
        ins=Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print("data has been written into the databse")

    return render(request,'contact.html')
    

