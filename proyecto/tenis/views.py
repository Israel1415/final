from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.
def loginpage(request):
    if request.method=='POST':
        password=request.POST['password']
        username=request.POST['username']
        user=authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            return redirect('/landing')
    elif request.method=='GET': 
        return render(request, 'login.html')

def landing(request):
    return render(request, 'pagina.html')


