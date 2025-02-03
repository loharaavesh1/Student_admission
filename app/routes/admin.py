import os
from flask import Blueprint, render_template, redirect, request, url_for, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import StudentApplication, User
from app.forms import AdminLoginForm, AdminSignupForm
from app.utils.pdf_generators import generate_admission_letter

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    existing_admin = User.query.first()
    if existing_admin:
        flash("Admin account already exists. Please log in.", "warning")
        return redirect(url_for('admin.login'))

    form = AdminSignupForm()
    if form.validate_on_submit():
        new_admin = User(username=form.username.data)
        new_admin.set_password(form.password.data)
        db.session.add(new_admin)
        db.session.commit()
        flash('Admin account created successfully. Please log in.', "success")
        return redirect(url_for('admin.login'))
    
    return render_template('admin/signup.html', form=form)


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        flash('Invalid username or password', "danger")
    return render_template('admin/login.html', form=form)


@admin_bp.route('/dashboard')
@login_required
def dashboard():
    applications = StudentApplication.query.all()
    return render_template('admin/dashboard.html', applications=applications)


@admin_bp.route('/application/<int:application_id>', methods=['GET', 'POST'])
@login_required
def review_application(application_id):
    application = StudentApplication.query.get_or_404(application_id)
    if request.method == 'POST':
        if 'approve' in request.form:
            application.status = 'approved'
            pdf_path = generate_admission_letter(application)  # Generate PDF
            application.pdf_path = pdf_path  # Save PDF path to database
            db.session.commit()
            flash('Application approved')
        elif 'reject' in request.form:
            application.status = 'rejected'
            db.session.commit()
            flash('Application rejected')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/application.html', application=application)

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('admin.login'))
