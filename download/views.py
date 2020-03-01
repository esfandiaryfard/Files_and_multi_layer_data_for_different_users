import os

from flask import request, jsonify, send_file
from flask_restful import Resource
from werkzeug.utils import secure_filename

from app import app


class Download(Resource):
    def get(self):
        username = request.args.get('username')
        filename = request.args.get('filename')
        path = os.path.join(username, filename)
        return send_file(path, as_attachment=True)
