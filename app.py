from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users20.db'
app.config['SECRET_KEY'] = 'ADFH898CEuoim^*(7nm(yn97qynME)('
db = SQLAlchemy(app)

# объект миграции
migrate = Migrate(app, db)

#объект логин-менеджер
#login_manager = LoginManager(app)
class UserLogin:
    def is_authenticated(self):
        return True #if user is authenticated

    def is_active(self):
        return True #if user is authenticated

    def is_anonymous(self):
        return False

    def get_id(self):
        return str()

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

        # Создание нового объекта пользователя
        new_user = User(username=username, email=email, password=password)
        if new_user:
            flash('Успешная регистрация!123', category='success')
        else:
            flash('Ошибка регистрации\nВозможно такой пользователь уже существует?', category='error')

        # Добавление пользователя в базу данных
        db.session.add(new_user)
        db.session.commit()

        # Создание профиля для пользователя
        new_profile = Profile(user_id=new_user.id)
        db.session.add(new_profile)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Здесь будет ваша логика аутентификации
    return render_template('login.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
