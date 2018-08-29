from django.shortcuts import render, HttpResponse, redirect
# 三件套 render 模板渲染
# HttpResponse 返回字符串
# redirect 重定向
import pymysql


# redirect  重定向
# Create your views here.


def index(request):
    # with open('templates/index','r') as f:
    #     data=f.read()
    print(request.method)

    # return HttpResponse('<h1>Hellw</h1>')
    return render(request, 'index.html')


def login111(request):
    # GET 一定要大写
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        name = request.POST['name']
        # 推荐用这种
        # request.POST  请求体的内容都在里面，字典形式
        # <QueryDict: {'name': ['123'], 'password': ['444']}>
        password = request.POST.get('password', None)
        conn = pymysql.connect(host='127.0.0.1', user='root', password="egon123", database='test', port=3306)

        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('select * from user where  name=%s and password=%s', [name, password])
        user = cursor.fetchone()
        if user:
            return HttpResponse('登录成功')
        # if name == 'lqz' and password == '123':
        #     # return HttpResponse('登录成功')
        #     return redirect('www.baidu.com')
        #     # return redirect('http://127.0.0.1:8000/index/')
        else:
            error = '用户名或密码错误'
            return render(request, 'login.html', {'error': error})


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


def login_submit(request):
    # pri nt(request.get_full_path())
    # print(request.method)
    print(request.POST)
    name = request.POST['name']
    # 推荐用这种
    # request.POST  请求体的内容都在里面，字典形式
    # <QueryDict: {'name': ['123'], 'password': ['444']}>
    password = request.POST.get('password', None)
    if name == 'lqz' and password == '123':
        # return HttpResponse('登录成功')
        return redirect('/index/')

    return redirect('/login/')
