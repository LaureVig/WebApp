import flask
from flask import Flask
from database.database import db, init_database
from database.models import *
from flask import url_for



# Ceci est un test !

app = Flask(__name__)
url_Laure = "sqlite:///C:\\Users\\laure\\Desktop\\WEBAPP\\WebApp\\database\\database.db"
url_Hugo = "sqlite:///C:\\Users\\hugop\\OneDrive\\Documents\\GitHub\\WebApp\\database\\database.db"
app.config["SQLALCHEMY_DATABASE_URI"] = url_Hugo
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)  # (1) flask prend en compte la base de donnee
with app.test_request_context():  # (2) bloc exécuté à l'initialisation de Flask
    print("test")
    init_database()



@app.route('/')
@app.route('/view/etudiants')
def view_etudiants():
    etudiants = Etudiant.query.all()
    return flask.render_template("template_etudiants.html.jinja2", etudiants=etudiants)


@app.route('/view/enseignants')
def view_enseignants():
    enseignants = Enseignant.query.all()
    return flask.render_template("template_enseignants.html.jinja2", enseignants=enseignants)


@app.route('/ajout/etudiant')
def ajout_etudiant():
    return flask.render_template("formulaire_etudiant.html.jinja2")


@app.route('/details/etudiant/<int:id>')
def detail_etudiant(id):
    etudiant=Etudiant.get_by_id(id)
    print(etudiant)
    return flask.render_template("details_etudiant.html.jinja2",etudiant=etudiant)


if __name__ == '__main__':
    app.run()
