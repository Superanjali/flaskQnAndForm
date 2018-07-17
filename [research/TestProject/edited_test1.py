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
        self.picture_list = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJtsYARqQQ3wu00tjf3J3mvSu0ykUPF8Zvb4zkiRH99E-KpeF-bw','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2lsDLO2vQzjXliPRLt5Apro-H5EkhfgrUQFSPpAE7UkfvdsVg','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWbB75H54u5J2D36_Ue1cSg5jpUZC_B0rIE76t0h8d7KY0NDlF','data:image/jpeg;base64,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']
        self.state = -2 #assume the last page with the end test so the next page is start test
        self.name = ''
        self.score = []
        self.question = ''
        self.reply = ''
        self.comments = ''
        self.previous_test = False
        self.wat_reply = 'Waiting for command'
        self.question_data ={}
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
            g.picture = g.picture_list[g.state]
            g.intentdes, qdata = wat.do_stuff('g Q' + str(g.state + 1))
            #question_data[]
        elif g.state == -2:
            # Compute socres
            values = []
            for i,elem in enumerate(g.score):
                values.append(wat.check_answer('Q'+str(i + 1),elem))
            g.join_score = ','.join(g.score)
            g.join_values = ','.join([str(x) for x in values])
            g.total_score = sum(elem[1] for elem in values)
            g.notrue = sum(elem[0] for elem in values)
            g.noq = len(values)
            # Read comments
            g.previous_test = True
        
        elif g.state == -1:
            qd = g.question_data
            qd = wat_api.get_question_data(qd, ['Q1', 'Q2', 'Q3', 'Q4'])
            print(json.dumps(qd, indent = 2))
             
            
    return flask.render_template('test_form.html', p = g)

@app.route('/admin', methods=['POST', 'GET'])
def admin():
    global g
    global wat
    if flask.request.method == 'POST':
        g.reply = flask.request.form['query']
        if g.reply == 'l':
            g.wat_reply = str(wat.question_list())
        else:
            g.wat_reply,_ = wat.do_stuff(g.reply)
        #Replace \n with <br>:
        #reply = reply.split('\n')
        #g.wat_reply = '<br>'.join(reply)
    else:
        g.wat_reply = 'Waiting for query'
    return flask.render_template('admin.html', p = g)

# %%
import json
'''
qd = {}    
qd = wat_api.get_question_data(qd, ['Q1', 'Q3'])
print(json.dumps(qd, indent = 2))
qd = wat_api.get_question_data(qd, ['Q2', 'Q4'])
print(json.dumps(qd, indent = 2))
'''
