from django.shortcuts import render,HttpResponse,redirect
from app01.models import *

# Create your views here.

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        birthday=request.POST.get('birthday')

        #第一种方式
        # user=UserInfo(name=name,password=password,gender=gender,birthday=birthday)
        # user.save()
        #第二种方式(推荐此方式)创建成功，会返回一个对象
        user=UserInfo.objects.create(name=name,password=password,gender=gender,birthday=birthday)
        print(user)

        return HttpResponse('注册成功')

            
    return render(request,'register.html')

def user_list(request):
    #把数据表里所有用户拿过来
    user_list=UserInfo.objects.all()
    return render(request,'user_list.html',{'user_list':user_list})