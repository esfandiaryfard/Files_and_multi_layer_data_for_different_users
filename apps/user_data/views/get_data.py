import json
import os

import connexion
from flask import request, jsonify

from app import app


class GetUserData(connexion.App):
    def __init__(self):
        connexion.App.__init__(self, 'get_user_data')

    def get(*args, **kwargs):
        username = request.args.get('username')
        if username is None:
            resp = jsonify(
                {
                    'message':'Username is essential! please enter username as '
                              'a query params'
                }
            )
            resp.status_code = 417
            return resp

        global_data = open('global_data.json')

        with global_data as gd:
            data = json.load(gd)

        # if user folder not exists just global data returns
        if not os.path.exists(os.path.join(app.path, username)):
            resp = jsonify(data)
            resp.status_code = 200
            return resp

        try:
            user_data = open(os.path.join(username, 'data.json'))
            with user_data as ud:
                json_data = json.load(ud)

            # get names of user data jsons
            data_names = []
            for items in json_data:
                data_names.append(items['name'])

            # get names of global data jsons
            global_names = []
            for items in data:
                global_names.append(items['name'])

            # if data with the same name exists in both global and user data
            # return user data
            for items in data_names:
                if items in global_names:
                    data[global_names.index(items)]['value'] = \
                                    json_data[data_names.index(items)]['value']
                else:
                    data.append(json_data[data_names.index(items)])

        # if user had no json data jusr global data returns
        except FileNotFoundError:
            resp = jsonify(data)
            resp.status_code = 200
            return resp

        resp = jsonify(data)
        resp.status_code = 200
        return resp