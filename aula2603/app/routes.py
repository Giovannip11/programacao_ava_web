from app import app,db
from urllib.parse import urlsplit
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm
from flask_login import login_user,logout_user,current_user,login_required

import sqlalchemy as sa
from app.models import User,Post
@app.route('/')
@app.route('/index')
@app.route('/user/<username>')
@login_required
def user (username):
    user = db.first_or_404(sa.select(User).where(User.username==username))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template ('user.html', user=user, posts=posts)

def index():
    user={'username': 'Giggio'}
    query = sa.select(Post)
    posts = db.session.scalars(query).all()

    return render_template('index.html',title="Home", user=user, posts=posts)

@app.route('/login', methods= ['GET','POST'])
def login():
    if current_user.is_authenticated:
      return redirect(url_for('index'))

    form=LoginForm()
    if form.validate_on_submit():
        user= db.session.scalar(
            sa.select(User).where(User.username==form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid usename or password')
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')

       
        return redirect(url_for(next_page))
    return render_template('login.html',title="Sign In", form=form)

@app.route('/logout')
def logout():
        logout_user()
        return redirect(url_for('index'))
        