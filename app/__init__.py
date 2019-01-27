# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.profile_controller import api as profile_ns
from .main.controller.patient_controller import api as patient_ns
from .main.controller.clinic_controller import api as clinic_ns
from .main.controller.appointment_controller import api as appointment_ns
from .main.controller.invoice_controller import api as invoice_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API FISIOWAVE',
          version='1.0',
          description='a rest api for fisiowave app'
          )

api.add_namespace(profile_ns, path='/profile')
api.add_namespace(patient_ns, path='/patient')
api.add_namespace(clinic_ns, path='/clinic')
api.add_namespace(appointment_ns, path='/appointment')
api.add_namespace(invoice_ns, path='/invoice')
api.add_namespace(auth_ns)
