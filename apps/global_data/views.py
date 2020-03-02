import json

from flask import request, jsonify
from flask_restful import Resource


class GlobalData(Resource):
    def post(self):
        name = request.form['name']
        value = request.form['value']
        data = []

        try:
            with open('global_data.json') as df:
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

        with open('global_data.json', 'w') as f:
            f.write(json.dumps(data, indent=2))

        resp = jsonify([{'message': 'Json file updated successfully'}, data])
        resp.status_code = 200
        return resp