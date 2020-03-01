from flask import Flask


app_path = 'E:/fmdfdu/api'

app = Flask(__name__)
app.debug = True

app.secret_key = "secret key"
app.config['app_path'] = app_path


