import datetime

from app.main import db
from app.main.model.profile import Profile


def generate_token(profile):
    try:
        # generate the auth token
        auth_token = profile.encode_auth_token(profile.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_new_profile(data):
    patient = Profile.query.filter_by(email=data['email']).first()
    if not patient:
        new_profile = Profile(
            name=data['name'],
            surname=data['surname'],
            username=data['username'],
            admin=data['admin'],
            email=data['email'],
            id_number=data['id_number'],
            company_name = data['company_name'],
            address=data['address'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_profile)
        return generate_token(new_profile)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Profile already exists.',
        }
        return response_object, 409


def get_profile_by_id(profile_id):
    return Profile.query.filter_by(id=profile_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
