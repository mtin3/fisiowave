from flask import request
from flask_restplus import Resource

from ..util.dto import ClinicDto
from ..service.clinic_service import save_new_clinic, get_all_clinics, get_clinics_by_query, get_clinic_by_id

api = ClinicDto.api
_clinic = ClinicDto.clinic


@api.route('/')
class ClinicList(Resource):
    @api.doc('list of registered clinics')
    @api.marshal_list_with(_clinic, envelope='data')
    def get(self):
        """List all registered clinics"""
        return get_all_clinics()

    @api.response(201, 'Clinic successfully created.')
    @api.doc('create a new clinic')
    @api.expect(_clinic, validate=True)
    def post(self):
        """Creates a new clinic """
        data = request.json
        return save_new_clinic(data=data)


@api.route('/<clinic_id>')
@api.param('clinic_id', 'The Clinic identifier')
@api.response(404, 'Clinic not found.')
class Clinic(Resource):
    @api.doc('get clinic by id')
    @api.marshal_with(_clinic)
    def get(self, clinic_id):
        """get a clinic given its identifier"""
        clinic = get_clinic_by_id(clinic_id)
        if not clinic:
            api.abort(404)
        else:
            return clinic


@api.route('/search')
@api.param('q', 'Query used for search')
class ClinicSearch(Resource):
    @api.doc('search clinics')
    @api.marshal_list_with(_clinic, envelope='data')
    @api.response(201, 'Clinic not found')
    def get(self):
        """List of clinics who satisfy the search"""
        query = request.args.get('q', None)
        return get_clinics_by_query(query)
