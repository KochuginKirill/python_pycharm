from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'


@app.route('/name/<name>/id/<number>/')
def func_name(name, number):
    number_user = int(number) * 100
    html = '''

    '''
    return f'<h1>Привет</h1>, <p><b>{name}</b> - <i>{number_user}</i></p>'


if __name__ == '__main__':
    app.run()
