import datetime

from sqlalchemy import or_

from app.main import db
from app.main.model.clinic import Clinic


def save_new_clinic(data):
    clinic = Clinic.query.filter_by(id_number=data['id_number']).first()
    if not clinic:
        new_clinic = Clinic(
            name=data['name'],
            email=data['email'],
            phone_number=data['phone_number'],
            id_number=data['id_number'],
            address=data['address'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_clinic)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Clinic already exists.',
        }
        return response_object, 409


def get_all_clinics():
    return Clinic.query.all()


def get_clinics_by_query(query):
    query = '%' + query + '%'
    return Clinic.query.filter(Clinic.name.ilike(query)).all()


def get_clinic_by_id(clinic_id):
    return Clinic.query.filter_by(id=clinic_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
