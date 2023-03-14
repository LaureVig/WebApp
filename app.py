import flask
from flask import Flask
from database.database import db, init_database
from database.models import *
from flask import url_for



# Ceci est un test !

app = Flask(__name__)
url_Laure = "sqlite:///C:\\Users\\laure\\Desktop\\WEBAPP\\WebApp\\database\\database.db"
url_Hugo = "sqlite:///C:\\Users\\hugop\\OneDrive\\Documents\\GitHub\\WebApp\\database\\database.db"
app.config["SQLALCHEMY_DATABASE_URI"] = url_Laure
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)  # (1) flask prend en compte la base de donnee
with app.test_request_context():  # (2) bloc exécuté à l'initialisation de Flask
    init_database()



@app.route('/')
@app.route('/view/etudiants')
def view_etudiants():
    etudiants = Etudiant.query.all()
    return flask.render_template("template_etudiants.html.jinja2", etudiants=etudiants)

def ajout_etudiant_valide(form):
    nom = flask.request.form.get("nom", "")
    prenom = flask.request.form.get("prenom", "")
    promotion = flask.request.form.get("promotion", "")
    taf1 = flask.request.form.get("taf1", "")
    taf2 = flask.request.form.get("taf2", "")
    stage1 = flask.request.form.get("stage1", "")
    stage2 = flask.request.form.get("stage2", "")
    stage3 = flask.request.form.get("stage3", "")
    mail = flask.request.form.get("mail", "")
    position = flask.request.form.get("position", "")

    result = True
    errors = []

    if nom == "":
        result = False
        errors += ["Le nom est requis"]
    if prenom == "":
        result = False
        errors += ["Le prenom est requis"]
    if promotion == "":
        result = False
        errors += ["Il manque la promotion"]
    if (taf1 != "" or taf2!= "") and taf1==taf2:
        result = False
        errors += ["pas les deux tafs identiques svp"]
    if mail == "":
        result = False
        errors += ["missing 'mail' parameter"]
    if (stage1 != "" or stage2 != "") and stage1 == stage2:
        result = False
        errors += ["pas les deux stages identiques svp"]
    if (stage3 != "" or stage2 != "") and stage3 == stage2:
        result = False
        errors += ["pas les deux stages identiques svp"]
    if (stage1 != "" or stage3 != "") and stage1 == stage3:
        result = False
        errors += ["pas les deux stages identiques svp"]
    return result, errors

def traitement_formulaire_etudiant(form):
    nom = flask.request.form.get("nom", "")
    prenom = flask.request.form.get("prenom", "")
    promotion = flask.request.form.get("promotion", "")
    taf1 = flask.request.form.get("taf1", "")
    taf2 = flask.request.form.get("taf2", "")
    stage1 = flask.request.form.get("stage1", "")
    stage2 = flask.request.form.get("stage2", "")
    stage3 = flask.request.form.get("stage3", "")
    mail = flask.request.form.get("mail", "")
    position = flask.request.form.get("position", "null")
    login = "admin"
    Etudiant.ajouterEtudiant(nom,prenom,mail,login,promotion,position,taf1,taf2,stage1,stage2,stage3)
    etudiants = Etudiant.query.all()
def afficher_formulaire_etudiant(form, errors):
    promotions = Promotion.getAllPromotion()
    promos = []
    for promotion in promotions:
        promos.append(str(promotion.pro_annee))
    stages = Stage.getAllStage()
    tafs = Taf.getAllTaf()
    positions = Position.getAllPosition()
    return flask.render_template("formulaire_etudiant.html.jinja2", promotions=promos, stages=stages, tafs=tafs,positions=positions, errors=errors,form=form)
@app.route('/ajout/etudiant',methods=["POST"])
def add_etudiant():
    form_est_valide, errors = ajout_etudiant_valide(flask.request.form)
    if not form_est_valide:
        return afficher_formulaire_etudiant(flask.request.form, errors)
    else:
        return traitement_formulaire_etudiant(flask.request.form)


@app.route('/view/enseignants')
def view_enseignants():
    enseignants = Enseignant.query.all()
    return flask.render_template("template_enseignants.html.jinja2", enseignants=enseignants)


@app.route('/ajout/etudiant')
def ajout_etudiant():
    promotions = Promotion.getAllPromotion()
    promos = []
    for promotion in promotions :
        promos.append(str(promotion.pro_annee))
    stages = Stage.getAllStage()
    tafs = Taf.getAllTaf()
    positions = Position.getAllPosition()
    form = None
    return flask.render_template("formulaire_etudiant.html.jinja2", promotions=promos, stages=stages, tafs=tafs,positions=positions, form=form)


@app.route('/details/etudiant/<int:id>')
def detail_etudiant(id):
    etudiant=Etudiant.get_by_id(id)
    taf1=Taf.get_by_id(etudiant.etu_taf1)
    taf2 = Taf.get_by_id(etudiant.etu_taf2)
    stage1 = Stage.get_by_id(etudiant.etu_stage1)
    stage2 = Stage.get_by_id(etudiant.etu_stage2)
    stage3 = Stage.get_by_id(etudiant.etu_stage3)
    position = Position.get_by_id(etudiant.etu_position_id)
    return flask.render_template("details_etudiant.html.jinja2",etudiant=etudiant, taf1=taf1, taf2=taf2, stage1=stage1,stage2=stage2,stage3=stage3,position=position)


if __name__ == '__main__':
    app.run()
