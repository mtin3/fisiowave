import datetime

from sqlalchemy import or_

from app.main import db
from app.main.model.patient import Patient


def save_new_patient(data):
    patient = Patient.query.filter_by(email=data['email']).first()
    if not patient:
        new_patient = Patient(
            name=data['name'],
            surname=data['surname'],
            alias=data['alias'],
            email=data['email'],
            phone_number=data['phone_number'],
            id_number=data['id_number'],
            address=data['address'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_patient)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Patient already exists.',
        }
        return response_object, 409


def get_all_patients():
    return Patient.query.all()


def get_patients_by_query(query):
    query = '%' + query + '%'
    return Patient.query.filter(or_(
        Patient.name.ilike(query), Patient.surname.ilike(query), Patient.alias.ilike(query)
    )).all()


def get_patient_by_id(patient_id):
    return Patient.query.filter_by(id=patient_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
