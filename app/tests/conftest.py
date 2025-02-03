import pytest
from app import create_app, db
from app.models import StudentApplication, User
from werkzeug.security import generate_password_hash

@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'WTF_CSRF_ENABLED': False
    })
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            admin = User(
                username='admin',
                password_hash=generate_password_hash('adminpass')
            )
            db.session.add(admin)
            db.session.commit()
            yield client
            db.drop_all()