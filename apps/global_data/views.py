import json

import connexion
from flask import request, jsonify


class GlobalData(connexion.App):
    def __init__(self):
        connexion.App.__init__(self, 'global_data')

    def post(*args, **kwargs):
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