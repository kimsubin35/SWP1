from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    number1 = d.get('number1', [''])[0] or 0
    number2 = d.get('number2', [''])[0] or 0

    if '' not in [number1, number2]:
        number1, number2 = int(number1), int(number2)
        Sum = number1 + number2
        Product = number1 * number2

    response_body = html % {
        'number1' : number1, 
	'number2' : number2, 
	'Sum' : Sum,
        'Product' : Product
   }

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]
