from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQl_USER'] = 'steven'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    msg = ''
    return render_template('index.html', msg='')

def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))

      account = cursor.fetchone()

   if account:
       session['loggedin'] = True
       session['id'] = account['id']
       session['username'] = account['username']

       return redirect(url_for('home'))
  else:
      msg = 'Incorrect username/password!'
@app.route('/pythonlogin/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)

   return redirect(url_for('login'))

@app.route('/pythonlogin/register', methods=['GET','POST'])
def register():

    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
    account = curso.fetchone()

    if account:
        msg = 'Account Already exists!'
    elif not re.match(r'[^@])+@[^@]+\.[^@]+', email):
       msg = 'Invalid email address!'
    elif not re.match(r'[A-Za-z0-9]+', email):
       msg = 'Username must contain only characters and numbers!'
    elif not username or password or not email:
       msg = 'Please fill out the form!'
    else:
        cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
        mysql.connection.commit()
        msg = 'You have successfully reqistered!'



    elif request.method == 'POST':

        msg = 'Please fill out  the form!'

    return render_template('register.html', msg=msg)
@app.route('/pythonlogin/home')
def home():

    if 'loggedin' in session:

        return render_template('home.html', username=session['username'])

    return redirect(url_for('login'))

@app.route('/pythonlogin/profile')
def profile():

    if 'loggedin' in session:

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()

        return render_template('profile.html', account=account)

    return redirect(url_for('login'))
