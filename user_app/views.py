from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username} successfully!')
            return redirect('home')
    else:
        form = UserCreationForm()    
    return render(request, 'auth/register.html',{'form':form} )