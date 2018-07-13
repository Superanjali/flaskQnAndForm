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

question_list = ['is anjali cute?','Are you crazy?','What do you want?']
state = -1
name = ''
score = 0
question = ''
reply = ''

@app.route('/test/<state>', methods=['POST', 'GET'])
def test(state):
    if flask.request.method == 'GET':
        state = -1
    elif flask.request.method == 'POST':
        # Processing inputs from old state
        if state == -1:
            name = flask.request.form['query']
            score = 0
        elif state >= 0:
            reply = flask.request.form['query']
            score += ',' + reply
        #Change state
        state += 1
        if state == len(question_list):
            state = -2

        # Computing outputs for your current state
        if state >= 0:
            question = question_list[state]
        
    return flask.render_template('test_form.html', **locals())
    
'''
-1: --
    -2: name, score
    : question, reply
'''    
