from flask import Flask
from flask_restful import Api

app_path = 'E:/fmdfdu/api'

app = Flask(__name__)
api = Api(app)

app.debug = True

app.secret_key = "secret key"
app.config['app_path'] = app_path

from download.views import Download
from upload.views import Upload
from user_data import views
from global_data.views import GlobalData

api.add_resource(Upload, '/api/upload')
api.add_resource(Download, '/api/download')
api.add_resource(views.SetUserData, '/api/setUserData')
api.add_resource(views.GetUserData, '/api/getUserData')
api.add_resource(GlobalData, '/api/setGlobalData')
