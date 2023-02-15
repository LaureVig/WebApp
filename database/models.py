from database.database import db

class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.Text, nullable=False)
    prenom = db.Column(db.Text, nullable=False)
    mail = db.Column(db.Text, nullable=False)
    promotion_id = db.Column(db.Integer, db.ForeignKey('promotion.id'))

    def __repr__(self):
        return '<Etudiant {}>'.format(self.nom)
    """taf1 = 
    taf2 = 
    stageA1
    stageA2
    stageA3"""

class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    annee = db.Column(db.Integer, nullable = False)
    promotion = db.relationship('Etudiant', backref='promotion')

    def __repr__(self):
        return '<Promotion {}>'.format(self.annee)