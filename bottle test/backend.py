from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host = 'localhost', port = 8000)
#Obviously doesn't work using ASK4...
