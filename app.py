import flask
from flask import Flask
from database.database import db, init_database
from database.models import *

app = Flask(__name__)
url_Laure="sqlite:///C:\\Users\\laure\\Desktop\\WEBAPP\\WebApp\\database\\database.db"
url_Hugo="sqlite:///C:\\Users\\hugop\\OneDrive\\Documents\\GitHub\\WebApp\\database\\database.db"
app.config["SQLALCHEMY_DATABASE_URI"] = url_Laure
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # (1) flask prend en compte la base de donnee
with app.test_request_context(): # (2) bloc exécuté à l'initialisation de Flask
 init_database()

@app.route('/')
def hello_world():
    tafs = Taf.query.all()
    etudiant_nom = Etudiant.get_etudiants_par_nom("Robidou")
    return flask.render_template("complex_view.jinja2", tafs=tafs, etudiants_nom=etudiant_nom )


if __name__ == '__main__':
    app.run()
