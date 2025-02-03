from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from datetime import datetime
from flask import current_app

def generate_admission_letter(application):
    try:
        # Create a unique filename
        filename = f"admission_{application.id}.pdf"
        
        # Define the path to save the PDF in the static folder
        pdf_folder = os.path.join(current_app.static_folder, 'uploads', 'pdfs')
        
        # Create the directory if it doesn't exist
        os.makedirs(pdf_folder, exist_ok=True)
        
        # Define the full path to save the PDF
        pdf_path = os.path.join(pdf_folder, filename)
        
        # Create the PDF
        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter
        
        # Add content to the PDF
        c.drawString(100, height - 100, "Admission Letter")
        c.drawString(100, height - 150, f"Name: {application.name}")
        c.drawString(100, height - 200, f"Email: {application.email}")
        c.drawString(100, height - 250, f"Admission Date: {datetime.now().strftime('%Y-%m-%d')}")
        c.save()
        
        # Return the relative path for database storage (relative to static folder)
        relative_pdf_path = os.path.relpath(pdf_path, current_app.static_folder).replace("\\", "/")
        return f"{relative_pdf_path}"
        
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return None
