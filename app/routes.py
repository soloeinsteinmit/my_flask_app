from flask import render_template, Blueprint, flash, redirect
from forms import LoginForm

microblog = Blueprint('main', __name__)

@microblog.route('/')
@microblog.route('/index')
def index():
    user = {'username': "Solomon"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!',
         },
        {
            'author': {'username': 'Susan'},
            'body': 'The avenger movie is cool!',
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@microblog.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title="Sign In", form=form)