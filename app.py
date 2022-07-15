#import the Flask class from the flask module
import row as row
from flask import Flask, render_template, redirect, request, url_for, session, flash, g
from functools import wraps
import sqlite3

# create the application object
app = Flask(__name__)

# config
# need secret key for session to work
# not ideal but a temp placeholder
app.secret_key = "my precious"

# another config for database
app.database = "sample.db"

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    # return "Hello, World!" # return a string

    # creates connection object for db connection
    # "g" is specific to flask and stores a temp object, like a db connection or currently logged in user
    g.db = connect_db()

    # Query db
    cur = g.db.execute('select * from posts')

    # cast to dictionary
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]

    # closes the db
    g.db.close()

    return render_template("index.html", posts=posts) # render a template


@app.route('/welcome')
def welcome():
    return render_template("welcome.html") # render a template

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))


# add in a function that connects to the database
# creates a database object we can interact with
def connect_db():
    return sqlite3.connect(app.database)





# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

