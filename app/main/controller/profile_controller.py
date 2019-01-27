from flask import request
from flask_restplus import Resource

from ..util.dto import ProfileDto
from ..service.profile_service import save_new_profile, get_profile_by_id

api = ProfileDto.api
_profile = ProfileDto.profile


@api.route('/')
class PatientCreate(Resource):
    @api.response(201, 'Profile successfully created.')
    @api.doc('create a new profile')
    @api.expect(_profile, validate=True)
    def post(self):
        """Creates a new Profile """
        data = request.json
        return save_new_profile(data=data)


@api.route('/<profile_id>')
@api.param('profile_id', 'The Profile identifier')
@api.response(404, 'Profile not found.')
class Profile(Resource):
    @api.doc('get profile by id')
    @api.marshal_with(_profile)
    def get(self, profile_id):
        """get a patient given its identifier"""
        profile = get_profile_by_id(profile_id)
        if not profile:
            api.abort(404)
        else:
            return profile
