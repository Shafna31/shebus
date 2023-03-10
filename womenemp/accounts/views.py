from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm
# Create your views here.
def home(request):
    return render(request,'index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful')
            return render(request,'index2.html')
        else:
            messages.error(request,'Invalid Credentials')
            return render(request,'log.html')
    return render(request,'log.html')
    

def reg(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.add_message(request, messages.INFO, f'Welcome {user.get_full_name()}!!!Your account has been registered successfully.')
            return render(request,'index2.html')
    else:
        form = SignUpForm()
    return render(request,'reg.html',{'form':form})

def ticket_book(request):
    return render(request,'ticketbook.html')
def payment(request):
    return render(request,'payment.html')
def userprofile(request):
    return render(request,'user.html')
def admin(request):
    return render(request,'admin.html')
def bus(request):
    return render(request,'buses.html')
def house(request):
    return render(request,'housewife.html')
def revenue(request):
    return render(request,'revenue.html')

def user_login1(request):
    return render(request,'login.html')