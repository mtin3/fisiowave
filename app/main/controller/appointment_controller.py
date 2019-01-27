from flask import request
from flask_restplus import Resource

from ..util.dto import AppointmentDto
from ..service.appointment_service import save_new_appointment, get_all_appointments, get_appointments_by_period,\
    get_appointments_by_patient, get_appointments_by_clinic, get_appointment_by_id

api = AppointmentDto.api
_appointment = AppointmentDto.appointment


@api.route('/')
class AppointmentList(Resource):
    @api.doc('list of all appointments')
    @api.marshal_list_with(_appointment, envelope='data')
    def get(self):
        """List all appointments"""
        return get_all_appointments()

    @api.response(201, 'Appointment successfully created.')
    @api.doc('create a new appointment')
    @api.expect(_appointment, validate=True)
    def post(self):
        """Creates a new appointment """
        data = request.json
        return save_new_appointment(data=data)


@api.route('/<appointment_id>')
@api.param('appointment_id', 'The appointment identifier')
@api.response(404, 'Appointment not found.')
class Appointment(Resource):
    @api.doc('get clinic by id')
    @api.marshal_with(_appointment)
    def get(self, appointment_id):
        """get an appointment given its identifier"""
        appointment = get_appointment_by_id(appointment_id)
        if not appointment:
            api.abort(404)
        else:
            return appointment


@api.route('/<patient_id>')
@api.param('patient_id', 'The patient identifier')
@api.response(201, 'Appointments not found.')
class AppointmentListByPatient(Resource):
    @api.doc('list of appointments by patient')
    @api.marshal_list_with(_appointment, envelope='data')
    def get(self, patient_id):
        """List all appointments from a patient"""
        return get_appointments_by_patient(patient_id)


@api.route('/<clinic_id>')
@api.param('clinic_id', 'The clinic identifier')
@api.response(201, 'Appointments not found.')
class AppointmentListByClinic(Resource):
    @api.doc('list of appointments by clinic')
    @api.marshal_list_with(_appointment, envelope='data')
    def get(self, clinic_id):
        """List all appointments from a clinic"""
        return get_appointments_by_clinic(clinic_id)


@api.route('/search')
@api.param('start', 'Start datetime for period')
@api.param('end', 'End datetime for period')
class AppointmentSearch(Resource):
    @api.doc('search appointments between two dates')
    @api.marshal_list_with(_appointment, envelope='data')
    @api.response(201, 'Appointments not found')
    def get(self):
        """List of appointment between to dates"""
        start_date = request.args.get('start', None)
        end_date = request.args.get('end', None)
        return get_appointments_by_period(start_date, end_date)
