'''
wsgiref模块把socket进行了封装，不需要手动写socket
封装了什么？
soc=socket.socket()
soc.bind(('127.0.0.1',8005))
soc.listen(5)
conn,addr=soc.accept()
'''

from wsgiref.simple_server import make_server

def my_server(environ,start_response):
    print(environ['PATH_INFO']) # 浏览器地址http://127.0.0.1:8010/TTTTT 打印了/TTTTT

    '''
    environ作用是已经拆分了请求头里的代码（\r\n等拆分），简化了拆分步骤，返回是字典
    '''
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 替代效果--->conn.send(b'HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n\r\n')     #HTTP/1.1 200 OK：响应首行，Content-Type:text/html：响应头，\r\n\r\n后面的东西为响应体

    return [b'hello web']

if __name__ == '__main__':
    my=make_server('127.0.0.1',8010,my_server)
    my.serve_forever()