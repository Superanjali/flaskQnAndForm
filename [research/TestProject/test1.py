import flask
import v04 as wat_api
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


class Globals():
    def __init__(self):
        self.question_list = ['State a reason why a scorpion is not an insect.','State a similarity between the characteristics of a frog and a crocodile.','The tadpole has a different breathing method compared to the adult frog. Explain why this is so.']
        self.state = -2 #assume the last page with the end test so the next page is start test
        self.name = ''
        self.score = []
        self.question = ''
        self.reply = ''
        self.comments = ''
        self.previous_test = False
        self.wat_reply = 'Waiting for command'
    def __setattr__(self,key,value):
        self.__dict__[key] = value
    def to_dict(self):
        return self.__dict__

wat = wat_api.Wat() 
g = Globals()

@app.route('/test', methods=['POST', 'GET'])
def test():
    global g
    global wat
    if flask.request.method == 'GET':
        g.state = -1
    elif flask.request.method == 'POST':
        # Processing inputs from old state
        if g.state == -1:
            g.name = flask.request.form['query']
            g.score = []
            g.reply = ''
        elif g.state == -2 and g.previous_test:
            g.comments = flask.request.form['query']
        elif g.state >= 0:
            g.reply = flask.request.form['query']
            g.score.append(g.reply)
    
        #Change state
        g.state += 1
        if g.state == len(g.question_list):
            g.state = -2

        # Computing outputs for your current state
        if g.state == 0:
            g.question_list = wat.question_list()
        if g.state >= 0:
            g.question = g.question_list[g.state]
            g.intentdes = wat.do_stuff('g Q' + str(g.state + 1))
        elif g.state == -2:
            # Compute socres
            values = []
            for i,elem in enumerate(g.score):
                values.append(wat.check_answer('Q'+str(i + 1),elem))
            pretty_values = [(elem[0],'%.2f' % elem[1]) for elem in values]
            #g.join_score = ','.join(g.score)
            g.join_values = ','.join([str(x) for x in pretty_values])
            g.total_score = sum(elem[1] for elem in values)
            g.notrue = sum(elem[0] for elem in values)
            g.noq = len(values)
            g.points = '%.2f' % sum(100*elem[1] for elem in values)
            g.total_points = g.noq*100
            # Read comments
            g.previous_test = True
            
    return flask.render_template('test_form.html', p = g)

@app.route('/admin', methods=['POST', 'GET'])
def admin():
    global g
    global wat
    if flask.request.method == 'POST':
        g.reply = flask.request.form['query']
        if g.reply == 'l':
            g.wat_reply = '\n'.join(wat.question_list())
        else:
            g.wat_reply = wat.do_stuff(g.reply)
        #Replace \n with <br>:
        #reply = reply.split('\n')
        #g.wat_reply = '<br>'.join(reply)
    else:
        g.wat_reply = 'Waiting for query'
    return flask.render_template('admin.html', p = g)
 