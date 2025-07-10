from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Booking
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myclean.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'

db.init_app(app)

# Create DB tablesfrom app.app import app
with app.app_context():
    db.create_all()


# login page as first page of web app
@app.route('/')
def home():
    return redirect(url_for('login'))

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
            flash('All fields are required.', 'error')
            return redirect(url_for('register'))

        # Check for existing user
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered.', 'error')
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

        flash('Registration successful!', 'success')
        return redirect(url_for('login'))  # redirect login

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard')) # go to main page after log in

        flash('Invalid email or password.', 'error')
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/book', methods=['GET', 'POST'])
def book_cleaner():
    # Check login for both GET and POST
    customer_id = session.get('user_id')
    if not customer_id:
        flash("You must be logged in to access booking.", 'error')
        return redirect('/login')

    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        address = request.form['address']
        notes = request.form['notes']

        booking_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

        booking = Booking(
            customer_id=customer_id,
            booking_datetime=booking_datetime,
            address=address,
            notes=notes,
            status="Pending"
        )
        db.session.add(booking)
        db.session.commit()

        flash("Booking confirmed!", 'success')
        return redirect('/book')

    return render_template('booking.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'error')
        return redirect(url_for('login'))
    return render_template('dashboard.html')

#to clear the session after user sings out
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

# load booking history based on user id
@app.route('/history')
def booking_history():
    user_id = session.get('user_id')
    if not user_id:
        flash("Please log in to view your booking history.", 'error')
        return redirect(url_for('login'))

    now = datetime.now()

    # Get past bookings with cleaner info using join
    bookings = db.session.query(Booking, User.full_name).outerjoin(
        User, Booking.cleaner_id == User.id
    ).filter(
        Booking.customer_id == user_id,
        Booking.booking_datetime < now
    ).order_by(Booking.booking_datetime.desc()).all()

    return render_template('booking_history.html', bookings=bookings)



if __name__ == '__main__':
    app.run(debug=True)

