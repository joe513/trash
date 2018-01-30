from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello from the outside'


@app.route('/yes/<name>')
def bomba(name):
    return 'This is yes! %s ' % name

