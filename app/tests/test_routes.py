from app.models import StudentApplication
from app import db

def test_admin_login(test_client):
    response = test_client.post('/admin/login', data={
        'username': 'admin',
        'password': 'adminpass'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Applications' in response.data

def test_application_approval(test_client):
    test_admin_login(test_client)
    with test_client.application.app_context():
        app = StudentApplication(
            name="Test App",
            email="test@example.com",
            phone="1234567890",
            status='pending'
        )
        db.session.add(app)
        db.session.commit()
    
    response = test_client.post(f'/admin/application/{app.id}', data={
        'approve': True
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'approved' in response.data