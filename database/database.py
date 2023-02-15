from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


def init_database():
    db.create_all()
    populate_database()

def populate_database():
    from database.models import Promotion, Etudiant
    new_promo = Promotion()
    new_promo.annee=2024
    db.session.add(new_promo)
    db.session.commit()
    new_student = Etudiant()
    new_student.nom = "Pichereau"
    new_student.prenom = "Hugo"
    new_student.mail = "hugo.pichereau@imt-atlantique.net"
    new_student.promotion_id =1
    # Ajout de la tache dans la base de donnees
    db.session.add(new_student)
    db.session.commit()  # Sauvegarde les informations dans la base de donnees