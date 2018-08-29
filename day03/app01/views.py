from django.shortcuts import render,HttpResponse
from app01.models import *
# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        birthday=request.POST.get('birthday')
        # 第一种方式
        # user=UserInfo(birthday=birthday,name=name,password=password,gender=gender)
        # user.save()
        # 第二种方式(推荐这种)创建成功，会返回一个对象
        user=UserInfo.objects.create(birthday=birthday,name=name,password=password,gender=gender)
        print(user)
        return HttpResponse('注册成功')

    return render(request,'register.html')



def user_list(request):

    # 把数据表里用户全拿回来
    user_list=UserInfo.objects.all()
    # print(type(user_list))
    #     # print(user_list[0].name)
    #     # print(user_list[0].password)



    return render(request,'user_list.html',{'user_list':user_list})