import string

from database.database import db


class Etudiant(db.Model):
    etu_id = db.Column(db.Integer, primary_key=True)
    etu_nom = db.Column(db.Text, nullable=False)
    etu_prenom = db.Column(db.Text, nullable=False)
    etu_mail = db.Column(db.Text, nullable=False)
    etu_promotion_id = db.Column(db.Integer, db.ForeignKey('promotion.pro_id'))
    etu_lien_taf = db.relationship('LienEtudiantTaf', backref='etudiant')

    def __repr__(self):
        return '<Etudiant {}>'.format(self.etu_nom)

    def get_etudiants_par_promo(annee:int):
        return db.session.query(Etudiant).join(Promotion).filter(Promotion.pro_annee==annee).all()

    def get_etudiants_par_taf(taf_id:int):
        return "Pas encore implémenté"

    def get_etudiants_par_nom(nom:string):
        return db.session.query(Etudiant).filter(Etudiant.etu_nom==nom)


class Promotion(db.Model):
    pro_id = db.Column(db.Integer, primary_key=True)
    pro_annee = db.Column(db.Integer, nullable=False)
    pro_promotion = db.relationship('Etudiant', backref='promotion')

    def __repr__(self):
        return '<Promotion {}>'.format(self.pro_annee)


class Taf(db.Model):
    taf_id = db.Column(db.Integer, primary_key=True)
    taf_nom = db.Column(db.Text, nullable=False)
    taf_description = db.Column(db.Text, nullable=False)
    taf_responsable_id = db.Column(db.Integer, db.ForeignKey('enseignant.ens_id'), nullable=False)
    taf_domaine_id = db.Column(db.Integer, db.ForeignKey('domaine.dom_id'), nullable=False)
    taf_lien_etudiant = db.relationship('LienEtudiantTaf', backref='taf')
    taf_lien_ue = db.relationship('LienUeTaf', backref='taf')

    def __repr__(self):
        return '<TAF {}>'.format(self.nom)


class LienEtudiantTaf(db.Model):
    let_etudiant_id = db.Column(db.Integer, db.ForeignKey('etudiant.etu_id'), primary_key=True)
    let_taf_id = db.Column(db.Integer, db.ForeignKey('taf.taf_id'), primary_key=True)
    let_annee = db.Column(db.Integer)


class Enseignant(db.Model):
    ens_id = db.Column(db.Integer, primary_key=True)
    ens_nom = db.Column(db.Text, nullable=False)
    ens_prenom = db.Column(db.Text, nullable=False)
    ens_mail = db.Column(db.Text, nullable=False)


class Domaine(db.Model):
    dom_id = db.Column(db.Integer, primary_key=True)
    dom_nom = db.Column(db.Text, nullable=False)


class Stage(db.Model):
    sta_id = db.Column(db.Integer, primary_key=True)
    sta_etudiant = db.Column(db.Integer, db.ForeignKey('etudiant.etu_id'))
    sta_entreprise = db.Column(db.Integer, db.ForeignKey('entreprise.ent_id'))
    sta_tuteur = db.Column(db.Integer, db.ForeignKey('personnel.per_id'))
    sta_mission = db.Column(db.Text)
    sta_duree = db.Column(db.Integer)
    sta_annee_etudiant = db.Column(db.Integer)
    sta_ville = db.Column(db.Text)


class Ue(db.Model):
    ue_id = db.Column(db.Integer, primary_key=True)
    ue_nom = db.Column(db.Text)
    ue_description = db.Column(db.Text)
    ue_responsable_id = db.Column(db.Integer, db.ForeignKey('enseignant.ens_id'), nullable=False)


class LienUeTaf(db.Model):
    lut_ue_id = db.Column(db.Integer, db.ForeignKey('ue.ue_id'), primary_key=True)
    lut_taf_id = db.Column(db.Integer, db.ForeignKey('taf.taf_id'), primary_key=True)

class Entreprise(db.Model):
    ent_id =db.Column(db.Integer, primary_key=True)
    ent_nom = db.Column(db.Text)

class Personnel(db.Model):
    per_id = db.Column(db.Integer, primary_key=True)
    per_nom =db.Column(db.Text)
    per_prenom =db.Column(db.Text)
    per_mail =db.Column(db.Text)
    per_entreprise = db.Column(db.Integer, db.ForeignKey('entreprise.ent_id'))