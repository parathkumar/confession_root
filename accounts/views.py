from django.shortcuts import render,redirect
from forms import SignUpForm
from django.views.generic import TemplateView
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
# Create your views here.
class signupclass(TemplateView):
     def get(self,request):
         form = SignUpForm()
         return render(request,'registration/signup.html',{'form':form})

     def post(self,request):
         form = SignUpForm(request.POST)
         if form.is_valid():
             user = form.save()
             '''email = form.cleaned_data.get('email')
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password1')'''
             #user = User.objects.create_user(username=username,email=email,password=password)
             user.save()
             '''user = authenticate(username = username,password = password)'''
             return redirect('/')

class ProfileDisplay(TemplateView):
    def get(self,request):
        return render(request,'registration/profile.html',{})

'''class logoutConfirmation(TemplateView):
    def get(self,request):
        return render(request,'registration/logout_confirmation.html',{})'''
