from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1 != pass2:
            return render(request, 'signup.html', {'error': 'Les mots de passe ne correspondent pas.'})
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        #send a welcome email
        subject='ahla bik fil plateforme mte3na'
        message=f'hello{uname},\n\thanks for registering we are excited for having you'
        from_email ='ghilanisaber191@gmail.com'
        recipient_list=[email]

        try:
            send_mail(subject,message,from_email,recipient_list)
        except Exception as e:
            return render (request,'login.html',{'error':'user created but email was not sent '})    
        
        return redirect ('login')



        
    return render (request,'signup.html')
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('username or password are inccorect')

        

    return render (request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')