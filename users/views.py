from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method== 'POST':
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            user=form.save()
            login(request,user)#para loguear al usuario automaticamente si es que se quiere
            return redirect('home')
    else:
        form = CustomUserCreationForm()     
    return render(request,'users/signup.html',{
        'form': form
    })

        