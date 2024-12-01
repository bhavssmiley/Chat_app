from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import SignupForm
def frontpage(request):
    return render(request,'base.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user) 
            return redirect('frontpage')
    else:
        form = SignupForm()
    return render(request,'Signup.html',{'form': form})
