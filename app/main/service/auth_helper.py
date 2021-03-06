from app.main.model.profile import Profile
from ..service.blacklist_service import save_token


class Auth:

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            profile = Profile.query.filter_by(email=data.get('email')).first()
            if profile and profile.check_password(data.get('password')):
                auth_token = profile.encode_auth_token(profile.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = Profile.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
            # get the auth token
            auth_token = new_request.headers.get('Authorization')
            if auth_token:
                resp = Profile.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    profile = Profile.query.filter_by(id=resp).first()
                    response_object = {
                        'status': 'success',
                        'data': {
                            'profile_id': profile.id,
                            'email': profile.email,
                            'admin': profile.admin,
                            'registered_on': str(profile.registered_on)
                        }
                    }
                    return response_object, 200
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Provide a valid auth token.'
                }
                return response_object, 401
