from flask import Flask
import connexion

app_path = 'E:/fmdfdu/api/'

app = connexion.App(__name__, specification_dir=app_path)
app.add_api('swagger/api.yaml')

app.path = app_path

app.debug = True

app.secret_key = "secret key"

if __name__ == "__main__":
    app.run()
