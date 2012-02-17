from piston.handler import BaseHandler
from piston.utils import throttle
from django.conf import settings
from pymongo import Connection
import simplejson as json
import utils

class TrialsHandler(BaseHandler):
    allowed_methods = ('GET',)

    @throttle(10, 30)
    def read(self, request, id=None):
        conn = utils.get_mongodb_connection()
        db = conn[settings.MONGODB_DBNAME]
        if id:
            data = db['trials'].find_one({'_id': id })
        else:
            data = list(db['trials'].find(limit=10))
        return data
