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

            data_item = []
            for items in data:
                if items['name'] == name:
                    items['value'] = value
                    data_item.append(items)

            data.extend(data_item)
            print(data)
        except FileNotFoundError:
            data.append(request.form)

        with open(os.path.join(username,'data.json'), 'w') as f:
            f.write(json.dumps(data, indent=2))        # path = os.path.join(username, filename)
        # return send_file(path, as_attachment=True)
