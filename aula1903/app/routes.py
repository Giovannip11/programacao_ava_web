from app import app,db
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
import sqlalchemy as sa
from app.models import User,Post
@app.route('/')
@app.route('/index')

def index():
    user={'username': 'Giggio'}
    query = sa.select(Post)
    posts = db.session.scalars(query).all()

    return render_template('index.html',title="Home", user=user, posts=posts)

@app.route('/login', methods= ['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login solicitado pelo usuario {}, Remember Me = {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('Login.html',title="Sign In", form=form)
        