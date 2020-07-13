import logging
import os

from flask_restplus import Api as _Api
from jsonschema import FormatChecker
from werkzeug.exceptions import HTTPException

log = logging.getLogger(__name__)

v = os.popen('git log | head -n 1')
commit = v.read().replace("commit ", "")[:7]

api = _Api(version='0.1#{}'.format(commit),
           default='',
           doc='/docs',
           title='Client Manager',
           description='',
           format_checker=FormatChecker())

@api.errorhandler
def default_error_handler(e):
    if isinstance(e, HTTPException):
        response = {'message': e.description}
        status_code = e.code
    else:
        response = {'message': 'Unhandled Exception'}
        status_code = 500

    log.exception(e)
    return response, status_code
