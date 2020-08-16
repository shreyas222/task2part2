  
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import  authenticate,login,logout







def signup(request):
    if request.method == 'POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        username = request.POST['username']
        email = request.POST['email']
        Phone_number = request.POST['P_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        listm = ['user already exist']
        listp = ['Passwords are not same']

             
        if password1==password2:
            if User.objects.filter(username=username).exists():
                return render(request,'userapp3/signup.html',{'i':'user already exsist'})
            else:
                users = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                users.save();
                return redirect('login')
        else:
             
            return render(request,'userapp3/signup.html',{'i':'paswwords are not same'})
    else:
        return render(request, 'userapp3/signup.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
        	auth.login(request, user)
        	return redirect('success')
        else:
            return render(request,'userapp3/login.html',{'i':'invalid username or password'})
    else:
            return render(request,'userapp3/login.html')

def success(request):
	return render(request,'userapp3/sucess.html')

def logout(request):
    auth.logout(request)
    return render(request,'userapp3/logout.html')