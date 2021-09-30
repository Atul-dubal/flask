import flask
from flask import Flask, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://id16911383_atul_dubal:UCYxldfabnIbzaUM@localhost:3306/id16911383_database'
db = SQLAlchemy(app)

class login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))

@app.route("/", methods = ['GET','POST'])
def atul():
   if(request.method=='POST'):
    username= request.form.get('username')
    email = request.form.get('email')
   # print(username + email)
     
    entry = login(username = username,email = email)
    db.session.add(entry)
    db.session.commit()
     
     
   return render_template('index1.html')
 

app.run(debug = False)
	