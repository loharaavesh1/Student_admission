# Student Admission System

## Project Overview
The Student Admission System is a web-based application that allows students to submit applications online and enables administrators to review, approve, or reject them. The system generates PDF admission letters for approved applicants and stores application data in a relational database.

### Key Features
- **Student Application Submission**: Allows students to fill out and submit applications.
- **Admin Dashboard**: Admins can review and manage applications.
- **Approval Workflow**: Applications can be approved or rejected.
- **PDF Generation**: Generates admission letters for approved applications.
- **Database Integration**: Stores all application data securely.

## Installation Instructions

### Prerequisites
- Python 3.8+
- Virtual Environment (recommended)
- MySQL or PostgreSQL database
- Node.js and npm (optional for frontend assets)

### Setup Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/loharaavesh1/Student_admission.git
   cd Student_admission
   ```

2. **Create and Activate a Virtual Environment:**
   
   **On macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **On Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   Create a `.env` file in the root directory and add:
   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   DATABASE_URL=postgresql://username:password@localhost:5432/admission_db
   SECRET_KEY=your_secret_key_here
   ```

5. **Set Up the Database:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the Application:**
   ```bash
   flask run
   ```
   Access the application at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage Instructions

### For Students
- Navigate to the application form.
- Fill in details and upload documents.
- Submit the form and receive confirmation.

### For Administrators
- Log in to the admin dashboard.
- Review applications and approve/reject them.
- Generate and download PDF admission letters for approved applications.

## Testing
To run tests, execute:
```bash
pytest
```

## Technology Stack
- **Backend:** Flask
- **Database:** MySQL / PostgreSQL
- **ORM:** SQLAlchemy
- **PDF Generation:** ReportLab, WeasyPrint
- **Frontend:** HTML, CSS, JavaScript
- **Testing:** PyTest

## Assumptions and Design Decisions
- **User Roles:** Students and Administrators.
- **Security:** Uses authentication and role-based access control.
- **Scalability:** Designed to support institutions of various sizes.
- **Customizability:** Forms and workflows can be modified as needed.

## Commands Reference

| Action | Command |
|--------|---------|
| Clone Repository | `git clone https://github.com/loharaavesh1/Student_admission.git` |
| Create Virtual Environment | `python -m venv venv` |
| Activate Virtual Environment (macOS/Linux) | `source venv/bin/activate` |
| Activate Virtual Environment (Windows) | `venv\Scripts\activate` |
| Install Dependencies | `pip install -r requirements.txt` |
| Set Up Database | `flask db init && flask db migrate && flask db upgrade` |
| Run Application | `flask run` |
| Run Tests | `pytest` |



