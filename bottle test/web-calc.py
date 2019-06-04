from bottle import route, run, template

@route('/sum/<num1:int>/<num2:int>')
def add(num1, num2):
    return template('<b>The sum of {{num1}} and {{num2}} is: {{sum}}</b>!', num1=num1, num2=num2, sum=(num1 + num2))

@route('/sub/<num1:int>/<num2:int>')
def sub(num1, num2):
    return template('<b>{{num1}} minus {{num2}} is: {{minus}}</b>!', num1=num1, num2=num2, minus=(num1 - num2))

@route('/prod/<num1:int>/<num2:int>')
def prod(num1, num2):
    return template('<b>The product of {{num1}} and {{num2}} is: {{mult}}</b>!', num1=num1, num2=num2, mult=(num1 * num2))

@route('/div/<num1:int>/<num2:int>')
def divide(num1, num2):
    return template('<b>{{num1}} divided by {{num2}} is: {{divided}}</b>!', num1=num1, num2=num2, divided=(num1 / num2))

@route('/mod/<num1:int>/<num2:int>')
def modulus(num1, num2):
    return template('<b>The modulus of {{num1}} and {{num2}} is: {{moduloed}}</b>!', num1=num1, num2=num2, moduloed=(num1%num2))

@route('/')
def home():
    return '<b>Add either "/sum/", "/sub/", "/prod/", "/div/" or "/mod/" to the URL followed by "<number1>/number2"</b>'

run(host = 'localhost', port = 8000)
