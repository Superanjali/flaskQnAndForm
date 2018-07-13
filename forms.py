# pythonspot.com
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from random import randint
import v04 as watapi

param_filename = 'input/science.txt' 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
wat = watapi.Wat()
 
class ReusableForm(Form):
    name = TextField('Answer:', validators=[validators.required()])
    #email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    #password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    #flash('')
    #<TO DO>: Select and display the question
    #this part is the bit that talks to the Watson code and gets the questions
    #You have to change the look and feel of this in hello html

    with open(param_filename,'r') as f:
        #mylines = f.readlines()
        quotes = f.read().splitlines()
    #quotes = [ ]    
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber]

    #TODO: Select and display an image that has to do with the questions

    
    #this part displays the form and displays the question on top of the form
    #for the bit that displays the question, you have to change the hello.html file
    
    form = ReusableForm(request.form)
 
    print (form.errors)
    if request.method == 'POST':
        answer=request.form['answer']
        #password=request.form['password']
        #email=request.form['email']
        result_str = wat.do_stuff(answer)
        flash(result_str)
        #print (answer, " ")

        #TODO: This part must check the variable answer that has been submitted
        #by the student and retuen a parameter
        '''
        if (answer=="abc"):
            # Save the comment here.
            flash('Answer is correct ')
        else:
            flash('This is wrong')
        '''
        
    return render_template('hello.html', **locals())
    #return render_template('hello.html', form=form)
 
if __name__ == "__main__":
    app.run()
