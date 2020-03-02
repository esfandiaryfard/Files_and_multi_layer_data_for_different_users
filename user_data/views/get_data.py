import json
import os

from flask import request, jsonify
from flask_restful import Resource

from app import app


class GetUserData(Resource):
    def get(self):
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
        if not os.path.exists(os.path.join(app.config['app_path'], username)):
            resp = jsonify(data)
            resp.status_code = 200
            return resp

        try:
            user_data = open(os.path.join(username, 'data.json'))
            with user_data as ud:
                json_data = json.load(ud)

            # combine user data and global data
            for items in json_data:
                data.append(items)

        # if user had no json data jusr global data returns
        except FileNotFoundError:
            resp = jsonify(data)
            resp.status_code = 200
            return resp


        resp = jsonify(data)
        resp.status_code = 200
        return resp