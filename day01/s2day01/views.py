
import pymysql
from jinja2 import Template
def index(response):
    with open('templates/index.html','r',encoding='utf-8')  as f:
        data=f.read()

    return data.encode('utf-8')

def time(response):
    import datetime
    now=datetime.datetime.now().strftime('%Y-%m-%d %X')
    with open('templates/two.html','r',encoding='utf-8') as f:
        data=f.read()
    data=data.replace('@@time@@',now)
    return data.encode('utf-8')


def user_list(response):
    # 连接数据库拿数据
    # 拿到一个数据库连接
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',database='test',password='123')
    # 拿到一个游标对象
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行sql
    cursor.execute('select * from user')
    # 把数据拿出来
    user_list=cursor.fetchall()
    print(user_list)
    with open('templates/user_list.html','r',encoding='utf-8')as f:
        data=f.read()
    # 生成一个模板对象，需要传字符串
    template=Template(data)
    # 相当于在执行data.replace()，返回替换完成的字符串
    data=template.render(user_list=user_list)



    return data.encode('utf-8')
def error(request):
    return '404'.encode('utf-8')


def favicon(request):
    with open('favicon.ico','rb') as f:
        data=f.read()
    return data