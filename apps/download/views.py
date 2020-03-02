import os

import connexion
from flask import request, send_file


class Download(connexion.App):
    def __init__(self):
        connexion.App.__init__(self, 'download')

    def get(*args, **kwargs):
        username = request.args.get('username')
        filename = request.args.get('filename')
        path = os.path.join(username, filename)
        return send_file(path, as_attachment=True)
