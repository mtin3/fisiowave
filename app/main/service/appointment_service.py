import datetime

from sqlalchemy import and_

from app.main import db
from app.main.model.appointment import Appointment


def save_new_appointment(data):
    new_appointment = Appointment(
        patient_id=data['patient_id'],
        date=data['date'],
        clinic_id=data['clinic_id'],
        address=data['address'],
        price=data['price'],
        invoice_id=None,
        registered_on=datetime.datetime.utcnow()
    )
    save_changes(new_appointment)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201


def get_all_appointments():
    return Appointment.query.all()


def get_appointments_by_period(start_date, end_date):
    return Appointment.query.filter(and_(Appointment.date >= start_date,
                                         Appointment.date <= end_date
                                         )
                                    ).all()


def get_appointments_by_patient(patient_id):
    return Appointment.query.filter_by(patient_id=patient_id).all()


def get_appointments_by_clinic(clinic_id):
    return Appointment.query.filter_by(clinic_id=clinic_id).all()


def get_appointment_by_id(appointment_id):
    return Appointment.query.filter_by(id=appointment_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
