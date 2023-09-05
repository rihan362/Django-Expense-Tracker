from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.template import loader
from shop.models import wings
import pandas as pd

# Create your views here.
def foam(request):
   return render(request,'templates\shop\index.html')

def main(request):
   print("hello")
   if request.method=="POST":
      add1=request.POST.get('fadd'),
      point1=request.POST.get('fpoint'),
      description1=request.POST.get('fdescription'),
      date1=request.POST.get('fdate'),
   
      
      print("hello")
      wing_value=wings()
      wing_value.add=add1
      wing_value.point=point1
      wing_value.description=description1
      wing_value.date=str(date1[0])
      print(type(date1))
      print(date1)
      # print(type(date1[0]))
      
      wing_value.save()
      return redirect('/show')
     
      
   return render(request,'templates/shop/tracker.html')
   
    
def handlelogin(request):
   if request.method=='POST':
      loginusername=request.POST['loginusername']
      loginpassword=request.POST['loginpassword']
      user=authenticate(username=loginusername,password=loginpassword)
      
      if user is  not None:
         login(request,user)
         messages.success(request,'Successfiully loggieni')
         return redirect('wings')
      else:
         messages.error(request,"Invalid")
         return redirect('')
      
      
      
   return HttpResponse('handlelogin')



def handlelogout(request):
   logout(request)
   messages.success(request,'logged out')
   return redirect('/')




def handlesignup(request):
   if request.method=='POST':
      username=request.POST['username']
      fname=request.POST['fname']
      lastname=request.POST['lastname']
      email=request.POST['email']
      pass1=request.POST['pass1']
      pass2=request.POST['pass2']
      
      myuser=User.objects.create_user(username,email,pass1)
      myuser.firstname=fname
      myuser.lastname=lastname
      myuser.password=pass1
      myuser.save()
      messages.success(request,'your account has crreated')
      return redirect('/wings')
   else:
      return HttpResponse('error 404s')
      
      
      
   
def represent(request):
   flap=[1000]
   flap=wings.objects.all().values()
   
   
   # template=loader.get_template('show.html')
   # flapping={
   #    'mymembers':flap,
   # }
   # return HttpResponse(template.render(context, request))
   context={
      'flap':flap,
   }
   return render(request,'templates\shop\show.html',context=context)
         
      

   
   

def bar(request):
   return render(request,'templates\shop\graph.html')
   
      
        