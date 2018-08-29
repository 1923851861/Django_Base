
from wsgiref.simple_server import make_server
import my_urls
from views import *


def my_server(environ, start_response):
    # print(environ)
    print(environ['PATH_INFO'])
    start_response('200 OK', [('Content-Type', 'text/html')])
    func=None
    for url in my_urls.urls:
        if url[0]==environ['PATH_INFO']:
            func=url[1]
            break
    if func:
        response=func(environ)
    else:
        response= error(environ)

    return [response,]


if __name__ == '__main__':

    my=make_server('127.0.0.1',8002,my_server)
    my.serve_forever()


