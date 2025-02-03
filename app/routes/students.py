from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from app import db
from app.models import StudentApplication
from app.forms import ApplicationForm
import os
from datetime import datetime

student_bp = Blueprint('student', __name__)

@student_bp.route('/')
def home():
    return redirect(url_for('student.apply')) 

@student_bp.route('/apply', methods=['GET', 'POST'])
def apply():
    form = ApplicationForm()
    if form.validate_on_submit():
        degree_file = form.degree_document.data
        id_file = form.id_proof.data
        
        degree_filename = secure_filename(degree_file.filename)
        id_filename = secure_filename(id_file.filename)
        
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Define folder paths
        degree_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], 'degrees')
        id_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], 'ids')

        # Create directories if they don’t exist
        os.makedirs(degree_folder, exist_ok=True)
        os.makedirs(id_folder, exist_ok=True)

        # Save files with proper path formatting
        degree_path = os.path.join(degree_folder, f"{timestamp}_{degree_filename}")
        id_path = os.path.join(id_folder, f"{timestamp}_{id_filename}")

        degree_file.save(degree_path)
        id_file.save(id_path)

        # Convert paths to relative for database storage (use forward slashes)
        relative_degree_path = os.path.relpath(degree_path, current_app.static_folder).replace("\\", "/")
        relative_id_path = os.path.relpath(id_path, current_app.static_folder).replace("\\", "/")

        application = StudentApplication(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            address=form.address.data,
            school=form.school.data,
            gpa=form.gpa.data,
            degree=form.degree.data,
            degree_path=f"uploads/{relative_degree_path}",  # Store correct relative path
            id_proof_path=f"uploads/{relative_id_path}"
        )

        db.session.add(application)
        db.session.commit()
        
        return redirect(url_for('student.status', application_id=application.id))

    return render_template('student/apply.html', form=form)

@student_bp.route('/status/<int:application_id>')
def status(application_id):
    application = StudentApplication.query.get_or_404(application_id)
    return render_template('student/status.html', application=application)
