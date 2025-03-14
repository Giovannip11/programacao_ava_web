from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user={'username': 'Giggio'}
    posts = [
        {
            'author': {'username': 'Joao'},
            'body': 'Belo dia em Vila Velha!'
        },
        {
            'author': {'username': 'Maria'},
            'body': 'Partiu Carnaval!'
        }

    ]

    return render_template('index.html',title="Home", user=user, posts=posts)

@app.route('/login', methods= ['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login solicitado pelo usuario {}, Remember Me = {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('Login.html',title="Sign In", form=form)
        