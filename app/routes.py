from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    transaktions = [('kassa_bank','reservdelar traktor',365),('varulager','färg',5764),('moms 25%','Omföring moms',465)]
    user = {'username':'Magnus'}
    return render_template('index.html',title='home',user=user,transaktions=transaktions)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data,form.remember_me.data))
        return redirect( url_for('index'))
    return render_template('login.html', title='Sign in',form=form)
