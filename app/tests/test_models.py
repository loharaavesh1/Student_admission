from app.models import User, StudentApplication
from werkzeug.security import check_password_hash

def test_user_password_hashing():
    user = User()
    user.set_password('testpass')
    assert user.check_password('testpass') is True
    assert user.check_password('wrongpass') is False

def test_application_creation():
    app = StudentApplication(
        name="Test User",
        email="test@example.com",
        phone="1234567890",
        address="Test Address",
        school="Test School",
        gpa=3.8,
        degree="Computer Science"
    )
    assert app.status == 'pending'