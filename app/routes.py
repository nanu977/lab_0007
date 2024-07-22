from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from app.models import User

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email, password=password).first()

        if user:
            # Handle successful login, e.g., redirect to a dashboard
            return redirect(url_for('main.secret'))
        else:
            flash('Invalid credentials. Please try again.')
            return redirect(url_for('main.login'))

    return render_template('login.html')



@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered.')
            return redirect(url_for('main.signup'))

        # Create new user
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.thank_you'))

    return render_template('signup.html')


@bp.route('/secret')
def secret():
    return render_template('secretpage.html')


@bp.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

