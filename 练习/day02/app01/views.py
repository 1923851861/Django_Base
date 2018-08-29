from django.shortcuts import render,HttpResponse,redirect   #redirect:重定向

import pymysql

# Create your views here.

def index(request): #request是请求的对象，包括属性与方法都可以获取

    # with open('templates/index','r') as f:
    #     data=f.read()
    # return HttpResponse('<h1>hello web</h1>')
    # 重复的文件操作可通过render来替代

    # print(request.method) 获取方法

    return render(request,'index.html') #由于settings中已经获取templates文件，直接输入文件下的html文件名即可

def login(request):
    #注意：GET和POST必须为大写字母
    if request.method=='GET':
        return render(request,'login.html',)
    elif request.method=='POST':

        # 两种取值方式，推荐使用第二种，请求体的内容都在里面，字典形式
        name = request.POST['name']  # 如果没有默认值，会报错
        password = request.POST.get('password', None)  # get可以在取字典时设置一个默认None(可自定义一个默认值)
        # 以上两个取值的'name'、'password'必须与login.hmtl表单中的'name'、'passwrd'对应
        # print(name,password)

        conn=pymysql.connect(host='127.0.0.1',user='root',password="123",database='test',port=3306) #注意：密码是双引号格式，设置mysql数据库相关信息
        cursor=conn.cursor(pymysql.cursors.DictCursor)  #将conn生成字典形式
        cursor.execute('select * from user where name=%s and password=%s',[name,password]) #使用[]形式传用户名密码值，当然也可以使用元组
        user=cursor.fetchone()
        if user:
            return HttpResponse('登陆成功')

        # if name == '123' and password == '123':  # name、password对应的是login.html表单中指定的'name'以及'password'的值
        #     # return HttpResponse('登录成功')
        #
        #     return redirect('/index/')  # 重定向后去往了/login/网址页面
        else:
            error='用户名或密码错误'
            return render(request,'login.html',{'error':error}) #第二个往后可传多个字典

'''
login函数的优化版本：
def login(request):
    error = ''
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST.get('password', None)
        conn = pymysql.connect(host='127.0.0.1', user='root', password="egon123", database='test', port=3306)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('select * from user where  name=%s and password=%s', [name, password])
        user = cursor.fetchone()
        if user:
            return HttpResponse('登录成功')
        else:
            error = '用户名或密码错误'
    return render(request, 'login.html', {'error': error})
'''


def login_submit(request):
    # print(request.get_full_path())  #返回包含查询字符串的请求路径。例如， "/music/bands/the_beatles/?print=true"
    # print(request.method) 查看是GET还是POST请求;此处结果：POST（因为已指定为POST请求）
    # print(request.POST) #结果：<QueryDict: {'name': ['111'], 'password': ['11']}>，非字典，但使用方式相同
    pass
