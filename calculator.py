#!/usr/bin/python

default = "No numbers set"

body = """<html>
<head>
<title>WSGI Calculator</title>
</head>
<body>
Your Answer is: %s. <usr/calculation>
<br>
</body>
</html>"""

def Calculation(callable=None, **params):
    import pprint
    pprint.pprint(environ)
    response_body = body % ()

    class Calculator():
        '''the calculator operations'''

        def add(self, request, a, b):
            '''Add two numbers'''
            return float(a) + float(b)

        def subtract(self, request, a, b):
            '''Subtract two numbers'''
            return float(a) - float(b)

        def multiply(self, request, a, b):
            '''Multiply two numbers'''
            return float(a) * float(b)

        def divide(self, request, a, b):
            '''Multiply two numbers'''
            return float(a) / float(b)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, Calculation)
    srv.serve_forever()
    #return wsgi.WSGIServer(Site(), **params)