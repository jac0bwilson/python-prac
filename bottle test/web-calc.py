from bottle import route, run, template

@route('/sum/<num1:int>/<num2:int>')
def add(num1, num2):
    return template('<b>The sum of those numbers is: {{sum}}</b>!', sum=(num1 + num2))

@route('sub/<num1:int>/<num2:int>')
def sub(num1, num2):
    return template('<b>The first number minus the second is: {{minus}}</b>!', minus=(num1 - num2))

@route('prod/<num1:int>/<num2:int>')
def prod(num1, num2):
    return template('<b>The product of those numbers is: {{mult}}</b>!', mult=(num1 * num2))

@route('div/<num1:int>/<num2:int>')
def divide(num1, num2):
    return template('<b>The first number divided by the second is: {{divided}}</b>!', divided=(num1 / num2))

@route('/')
def home():
    return '<b>Add either "/sum/", "/sub/", "/prod/" or "/div/" to the URL followed by "<number1>/number2"</b>'

run(host = 'localhost', port = 8000)
