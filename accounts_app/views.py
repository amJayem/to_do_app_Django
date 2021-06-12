from django.contrib import auth
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def user_log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            print('username: ', username)
            login(request,user)
            return redirect('home')

        else:
            print("Invalid username or password!!")

    return render(request,'auth/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')