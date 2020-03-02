from flask import Flask
import connexion

app_path = '/home/annabelle/Files_and_multi_layer_data_for_different_users/'

app = connexion.App(__name__, specification_dir=app_path)
app.add_api('swagger/api.yaml')


app.debug = True

app.secret_key = "secret key"
# app.config['app_path'] = app_path


# from apps.download.views import Download
# from apps.upload.views import Upload
# from apps.user_data import views
# from apps.global_data.views import GlobalData

# api.add_resource(Upload, '/api/upload')
# api.add_resource(Download, '/api/download')
# api.add_resource(views.SetUserData, '/api/setUserData')
# api.add_resource(views.GetUserData, '/api/getUserData')
# api.add_resource(GlobalData, '/api/setGlobalData')
