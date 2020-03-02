import os

from flask import request, jsonify, send_file
from flask_restful import Resource
from werkzeug.utils import secure_filename

from app import app
import json


class UserData(Resource):
    def post(self):
        username = request.args.get('username')
        name = request.form['name']
        value = request.form['value']
        data = []
        if not os.path.exists(os.path.join(app.config['app_path'], username)):
            os.makedirs(os.path.join(app.config['app_path'], username))

        try:
            data_file = open(os.path.join(username, 'data.json'))
            with data_file as df:
                data = json.load(df)

            names = []
            for items in data:
                names.append(items['name'])

            if name in names:
                data[names.index(name)]['value'] = value
            else:
                data.append(request.form.to_dict(flat=True))

        except FileNotFoundError:
            data.append(request.form)

        with open(os.path.join(username,'data.json'), 'w') as f:
            f.write(json.dumps(data, indent=2))

        resp = jsonify([{'message': 'Json file updated successfully'}, data])
        resp.status_code = 200
        return resp