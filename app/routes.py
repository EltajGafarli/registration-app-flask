from app import app
from flask import render_template
from app.forms import SignUpForm
from app.forms import LoginForm
from app.models import Users
from flask import redirect,url_for
from flask import jsonify,url_for
from flask import flash
from flask import request

from flask_login import login_user

from devtools import debug

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/signup',methods=["GET","POST"])
def signup():
    form = SignUpForm()
    
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        user = {"username":username,"email":email}
        Users.add_user(form.username.data,form.email.data,form.password1.data)
        
        return render_template('profile.html',user = user)
        
    return render_template('signin.html',form = form)

@app.route('/login',methods=["GET","POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user  = Users.query.filter_by(username=form.username.data).first()
            if user and user.check_user(form.password.data):
                login_user(user=user)
                return render_template('profile.html',user = user)
            
    return render_template('login.html',form = form)
