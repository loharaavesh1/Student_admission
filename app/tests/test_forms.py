from app.forms import ApplicationForm, AdminLoginForm

def test_application_form_validation():
    form = ApplicationForm(data={
        'name': 'John Doe',
        'email': 'invalid-email',
        'phone': '1234567890',
        'address': '123 Main St',
        'school': 'Test School',
        'gpa': 3.5,
        'degree': 'Computer Science'
    })
    assert not form.validate()
    assert 'email' in form.errors