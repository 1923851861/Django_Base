import socket

soc=socket.socket()
soc.bind(('127.0.0.1',8003))
soc.listen(5)

while True:
    print('监听8003端口')
    conn,addr=soc.accept()

    data=conn.recv(1024)
    # 转换成str类型
    data=str(data,encoding='utf-8')
    print(data)
    request_list=data.split('\r\n')
    first_list=request_list[0].split(' ')
    conn.send(b'HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n\r\n')
    if first_list[1]=='/index':
        # conn.send('<h1>index</h1><img src="https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike92%2C5%2C5%2C92%2C30/sign=775f519ac08065386fe7ac41f6b4ca21/fd039245d688d43f63d84526771ed21b0ff43bf5.jpg">'.encode('utf-8'))
        with open('index.html','rb')as f:
            data=f.read()
        conn.send(data)
    elif first_list[1]=='/two':
        with open('two.html','r',encoding='utf-8')as f:
            data=f.read()
        import datetime
        now=datetime.datetime.now().strftime('%Y-%m-%d %X')
        data=data.replace('@@time@@',now)
        conn.send(data.encode('utf-8'))
    else:
        conn.send(b'404')


    # print(data)
    #
    # conn.send(b'HTTP/1.1 200 OK \r\n\r\nhello web')
    conn.close()


'''
# 请求首行：请求类型  请求地址  请求协议
GET /index HTTP/1.1\r\n
# 请求头
Host: 127.0.0.1:8001\r\n
Connection: keep-alive\r\n
Cache-Control: max-age=0\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n\r\n'

# 请求体
。。。。
'''
