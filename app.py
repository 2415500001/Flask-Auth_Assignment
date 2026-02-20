import os
from flask import Flask ,render_template,request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)

database_url = os.environ.get('DATABASE_URL')
if database_url and database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url or os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///charlie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')

@app.route('/')
def home ():
    return render_template("index.html")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

with app.app_context():
    db.create_all()



@app.route('/login', methods=['GET', 'POST'])
def login ():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect('/dashboard')
        else:
            flash('Invalid email or password.', 'danger')
            return redirect('/login')

    return render_template("login.html")

@app.route('/register' , methods=['GET', 'POST'])
def register ():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        if not name:
            flash('Name is required.', 'danger')
            return redirect('/register')

        if not email:
            flash('Email is required.', 'danger')
            return redirect('/register')

        if not password:
            flash('Password is required.', 'danger')
            return redirect('/register')

        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'danger')
            return redirect('/register')

        if User.query.filter_by(email=email).first():
            flash('Email already registered. Please log in.', 'danger')
            return redirect('/register')

        new_user = User(name, email, password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect('/login')
    
    return render_template("register.html")
    

@app.route('/dashboard')
def dashboard ():    
    if 'user_id' not in session:
        return redirect('/login')
    
    return render_template("dashboard.html")
if __name__=='__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)