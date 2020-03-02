import os

from flask import request, jsonify
from werkzeug.utils import secure_filename
import connexion
from app import app


class Upload(connexion.App):
    def post(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp

        file = request.files['file']

        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp

        filename = secure_filename(file.filename)
        username = request.args.get('username')

        # Create a folder for give username if not exists
        if not os.path.exists(os.path.join(app.config['app_path'], username)):
            os.makedirs(os.path.join(app.config['app_path'], username))

        file.save(os.path.join(
            app.config['app_path'],
            username,
            filename
        )
        )
        resp = jsonify({'message': 'File successfully uploaded'})
        resp.status_code = 201
        return resp
