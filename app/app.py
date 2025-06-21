from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myclean.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'

db.init_app(app)

# Create DB tables
with app.app_context():
    db.create_all()

# Route to render registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        # Basic validation
        if not full_name or not email or not password or not role:
            flash('All fields are required.')
            return redirect(url_for('register'))

        # Check for existing user
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered.')
            return redirect(url_for('register'))

        # Hash password and save user
        hashed_password = generate_password_hash(password)
        new_user = User(
            full_name=full_name,
            email=email,
            password_hash=hashed_password,
            role=role
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!')
        return redirect(url_for('register'))  # Or redirect to login

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

