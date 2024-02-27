# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import math
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users20.db'
db = SQLAlchemy(app)

#объект миграции
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100))
    age = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(username, email)

        # Create a new user object
        new_user = User(username=username, email=email, password=password)

        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()

        # Create a profile for the user
        new_profile = Profile(user_id=new_user.id)
        db.session.add(new_profile)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('register.html')


@app.route('/')
def index():
    return render_template('index.html')

print(math.sqrt(4))
if __name__ == '__main__':
    app.run(debug=True)

#commit1
