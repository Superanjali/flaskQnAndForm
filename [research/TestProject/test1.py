import flask
#from flask import render_template
#from flask import Flask

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, test World!'

@app.route('/pages/<number>')
def pg1(number):
    return 'You are on page %s' % number

with app.test_request_context():
    print(flask.url_for('pg1', number='test here'))

@app.route('/index')
def myindex():
    #return flask.render_template('index.html', title=None, user='Sohia')
    return flask.render_template('index.html', user = 'Anjali', marks = 60)

@app.route('/test', methods=['POST', 'GET'])
def test():
    if flask.request.method == 'POST':
        text = flask.request.form['query']
    else:
        text = 'Waiting user input'
    print(text)
    return flask.render_template('test_form.html', reply = text)

