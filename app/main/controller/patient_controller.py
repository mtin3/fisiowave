from flask import request
from flask_restplus import Resource

from ..util.dto import PatientDto
from ..service.patient_service import save_new_patient, get_all_patients, get_patients_by_query, get_patient_by_id

api = PatientDto.api
_patient = PatientDto.patient


@api.route('/')
class PatientList(Resource):
    @api.doc('list of registered patients')
    @api.marshal_list_with(_patient, envelope='data')
    def get(self):
        """List all registered patients"""
        return get_all_patients()

    @api.response(201, 'Patient successfully created.')
    @api.doc('create a new patient')
    @api.expect(_patient, validate=True)
    def post(self):
        """Creates a new Patient """
        data = request.json
        return save_new_patient(data=data)


@api.route('/<patient_id>')
@api.param('patient_id', 'The Patient identifier')
@api.response(404, 'Patient not found.')
class Patient(Resource):
    @api.doc('get patient by id')
    @api.marshal_with(_patient)
    def get(self, patient_id):
        """get a patient given its identifier"""
        patient = get_patient_by_id(patient_id)
        if not patient:
            api.abort(404)
        else:
            return patient


@api.route('/search')
@api.param('q', 'Query used for search')
class PatientSearch(Resource):
    @api.doc('search patient')
    @api.marshal_list_with(_patient, envelope='data')
    @api.response(201, 'Patient not found')
    def get(self):
        """List of patients who satisfy the search"""
        query = request.args.get('q', None)
        return get_patients_by_query(query)
