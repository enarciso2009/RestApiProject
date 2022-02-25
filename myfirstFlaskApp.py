
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_wtf.csrf import CSRFError, CSRFProtect
from flask_pymongo import PyMongo, pymongo

app = Flask(__name__)

csrf = CSRFProtect()
csrf.init_app(app)

app.config['SECRET_KEY'] = 'thisisascretkey'
app.config['MONGO DBNAME'] = "myFirstDatabase"
app.config['MONGO_URI'] = "mongodb+srv://<username>:<password>@cluster0.vwell.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


mongo = PyMongo(app)


@app.route('/')
def home():
    if 'user' in session:
        return render_template('message.html', username=session['user'])
    return redirect(url_for('login_func'))

@app.route('/redirected')
def redirected_req():
    return "your request has been redirected"

@app.route('/login', methods=['GET','POST'])
def login_func():
    if request.method == 'GET':
        message='hello there'
        return render_template('login.html', message=message)
        print('estou aqui ')
    username = request.form['username']
    password = request.form['password']

    mongo.db.users.insert({'username':username, 'password':password})

    print(f'usuario {username} and senha {password}')
    session['user']=username
    return render_template('message.html', username=session['user'])

@app.route('/logout')
def logout():
    session.pop('user',None)
    return render_template('logout.html')


if __name__=='__main__':
    app.run(debug=False)