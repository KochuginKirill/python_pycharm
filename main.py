from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def say_hello():
    return render_template('index.html')


@app.route('/test/')
def say_start(name='noname'):
    html = '''
    <h1>Hi, Tom</h1>
    <p> Lots of text </p>
    '''
    return html


if __name__ == '__main__':
    app.run()
#
#
# @app.route('/name/<name>/id/<number>/')
# def func_name(name, number):
#     number_user = int(number) * 100
#     html = '''
#
#     '''
#     return f'<h1>Привет</h1>, <p><b>{name}</b> - <i>{number_user}</i></p>'
#
#
# if __name__ == '__main__':
#     app.run()

def openOrSenior(data):
    res = []
    for i in data:
      if i[0] >= 55 and i[1] > 7:
        res.append("Senior")
      else:
        res.append("Open")
    return res
