from flask_restplus import Namespace, fields


class ProfileDto:
    api = Namespace('profile', description='profile related operations')
    profile = api.model('profile', {
        'name': fields.String(required=True, description='profile name'),
        'surname': fields.String(required=True, description='profile surname'),
        'username': fields.String(description='profile username'),
        'admin': fields.Boolean(description='is this profile admin?'),
        'email': fields.String(required=True, description='profile email address'),
        'company_name': fields.String(description='profile company_name'),
        'id_number': fields.String(description='profile identification number'),
        'address': fields.String(description='profile address')
    })


class PatientDto:
    api = Namespace('patient', description='patient related operations')
    patient = api.model('patient', {
        'name': fields.String(required=True, description='patient name'),
        'surname': fields.String(required=True, description='patient surname'),
        'alias': fields.String(description='patient alias'),
        'email': fields.String(required=True, description='patient email address'),
        'phone_number': fields.String(description='patient phone number'),
        'id_number': fields.String(description='patient identification number'),
        'address': fields.String(description='patient address')
    })


class ClinicDto:
    api = Namespace('clinic', description='clinic related operations')
    clinic = api.model('clinic', {
        'name': fields.String(required=True, description='clinic name'),
        'email': fields.String(required=True, description='clinic email address'),
        'phone_number': fields.String(description='clinic phone number'),
        'id_number': fields.String(description='clinic identification number'),
        'address': fields.String(description='clinic address')
    })


class AppointmentDto:
    api = Namespace('appointment', description='appointment related operations')
    appointment = api.model('appointment', {
        'patient_id': fields.Integer(required=True, description='patient'),
        'date': fields.DateTime(required=True, description='appointment date'),
        'clinic_id': fields.Integer(description='clinic'),
        'price': fields.Float(description='price'),
        'address': fields.String(description='appointment address')
    })


class InvoiceDto:
    api = Namespace('invoice', description='appointment related operations')
    invoice = api.model('invoice', {
        'invoice_number': fields.String(requiered=True, description='Invoice number'),
        'patient_id': fields.Integer(description='patient'),
        'date': fields.Date(required=True, description='invoice date'),
        'clinic_id': fields.Integer(description='clinic'),
        'subtotal': fields.Float(required=True, description='subtotal'),
        'VAT': fields.Float(required=True, description='VAT'),
        'total': fields.Float(required=True, description='total')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })