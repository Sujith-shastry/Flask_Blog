from flask import Flask, render_template ,url_for, flash, redirect
from forms import Registrationform, Loginform
import os
app = Flask(__name__)
app = Flask(__name__, template_folder='template')


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

posts=[
   {
      'author' : 'Sujith.G',
      'title' : 'Blog Post1',
      'Content' : 'First_Post',
      'date_posted' : 'April 02, 2020'
   },
   {
      'author' : 'Sujith.G. Shastry',
      'title' : 'Blog Post2',
      'Content' : 'Second_Post',
      'date_posted' : 'April 01, 2020'
   }
]

@app.route("/")

@app.route("/home")
def home():
   return render_template('home.html',posts=posts)

@app.route("/about" ,methods=['GET', 'POST'])
def about():
   return render_template('about.html',title='About Page')

@app.route("/register" , methods=['GET', 'POST'])
def register():
   form=Registrationform()
   if form.validate_on_submit():
      str="Account Created for {} !!"
      flash(str.format(form.username.data), 'success')
      return redirect(url_for('home'))
   return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET', 'POST'])
def login():
   form=Loginform()
   if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged Sucessfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check Email and password', 'danger')
   return render_template('login.html',title='Login',form=form)



if __name__=='__main__':
	app.run(debug=True)


