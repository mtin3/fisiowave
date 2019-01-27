import datetime

from sqlalchemy import or_

from app.main import db
from app.main.model.invoice import Invoice


def save_new_invoice(data):
    global new_invoice
    invoice = Invoice.query.filter_by(invoice_number=data['invoice_number']).first()
    if not invoice:
        if 'patient_id' in data and 'clinic_id' in data:
            new_invoice = Invoice(
                invoice_number=data['invoice_number'],
                date=data['date'],
                patient_id=data['patient_id'],
                clinic_id=data['clinic_id'],
                subtotal=data['subtotal'],
                VAT=data['VAT'],
                total=data['total'],
                registered_on=datetime.datetime.utcnow()
            )
        elif 'patient_id' in data and 'clinic_id' not in data:
            new_invoice = Invoice(
                invoice_number=data['invoice_number'],
                date=data['date'],
                patient_id=data['patient_id'],
                subtotal=data['subtotal'],
                VAT=data['VAT'],
                total=data['total'],
                registered_on=datetime.datetime.utcnow()
            )
        elif 'patient_id' not in data and 'clinic_id' in data:
            new_invoice = Invoice(
                invoice_number=data['invoice_number'],
                date=data['date'],
                clinic_id=data['clinic_id'],
                subtotal=data['subtotal'],
                VAT=data['VAT'],
                total=data['total'],
                registered_on=datetime.datetime.utcnow()
            )
        save_changes(new_invoice)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Invoice already exists.',
        }
        return response_object, 409


def get_all_invoices():
    return Invoice.query.all()


def get_invoices_by_query(query):
    query = '%' + query + '%'
    return Invoice.query.filter(or_(Invoice.invoice_number.ilike(query))).all()


def get_invoice_by_id(invoice_id):
    return Invoice.query.filter_by(id=invoice_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
