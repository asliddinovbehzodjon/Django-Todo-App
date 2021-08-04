from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Todo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
  return render(request,'home.html')
@login_required(login_url='login')
def todo(request):
  if request.method=='POST':
    work=request.POST.get('work')
    user=request.user
    info=Todo(todo=work,user=user)
    info.save()
    return redirect('/todo')
  todos=Todo.objects.filter(user=request.user).all()
  return render(request,'todo.html',{'todos':todos})
def loginpage(request):
  if request.user.is_authenticated:
      return redirect('/')
  if request.method=='POST':
    username=request.POST.get('name')
    password=request.POST.get('password')
    user=authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      return redirect('/todo')
    else:
      form='Xato username yoki parol!'
      return render(request,'login.html',{'form':form})
  return render(request,'login.html')
def registerpage(request):
  if request.user.is_authenticated:
      return redirect('/')
  if request.method=='POST':
    username=request.POST['name']
    password=request.POST['password']
    password2=request.POST['password2']
    if User.objects.filter(username=username).exists():
      form='Bu username bilan allaqachon akkaunt ochilgan!'
      return render(request,'register.html',{'form':form})
    if password != password2:
      form='Parollar bir xil emas!'
      return render(request,'register.html',{'form':form})
    if password==password2:
      user=User.objects.create_user(username=username,password=password)
      user.save()
      return redirect('/todo')

  return render(request,'register.html')
def logoutuser(request):
  logout(request)
  return redirect('/login')
def delete(request,user,id):
  Todo.objects.filter(user=user,id=id).delete()
  return redirect('/todo')
def update(request,user,id):
  if request.method=='POST':
     work=request.POST['work']
     Todo.objects.filter(user=user,id=id).update(todo=work)
     return redirect('/todo')
  form=Todo.objects.get(user=user,id=id)
  return render(request,'update.html',{'form':form})
