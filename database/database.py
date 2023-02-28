from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


def init_database():
    from database.models import Promotion, Etudiant, Taf
    db.drop_all()
    print("drop ?")
    db.create_all()
    print("create ?")
    print(db.get_tables_for_bind())
    populate_database()

def populate_database():
    from database.models import Promotion, Etudiant, Taf,Stage, Entreprise, Personnel
    new_taf = Taf()
    new_taf.taf_nom='DCL'
    new_taf.taf_description="Developpement Collaboratif de Logiciels"
    new_taf.taf_responsable_id=1
    new_taf.taf_domaine_id=1
    db.session.add(new_taf)

    new_promo = Promotion()
    new_promo.pro_annee=2024
    db.session.add(new_promo)

    new_student = Etudiant()
    new_student.etu_nom = "Pichereau"
    new_student.etu_prenom = "Hugo"
    new_student.etu_mail = "hugo.pichereau@imt-atlantique.net"
    new_student.etu_promotion_id =1
    # Ajout de la tache dans la base de donnees
    db.session.add(new_student)

    new_student2 = Etudiant()
    new_student2.etu_nom = "Vigouroux"
    new_student2.etu_prenom = "Laure"
    new_student2.etu_mail = "laure.vigouroux@imt-atlantique.net"
    new_student2.etu_promotion_id = 1
    # Ajout de la tache dans la base de donnees
    db.session.add(new_student2)

    new_student3 = Etudiant()
    new_student3.etu_nom = "Robidou"
    new_student3.etu_prenom = "Guillaume"
    new_student3.etu_mail = "guillaume.robidou@imt-atlantique.net"
    new_student3.etu_promotion_id = 1
    # Ajout de la tache dans la base de donnees
    db.session.add(new_student3)

    new_entreprise = Entreprise()
    new_entreprise.ent_nom="Trecobat"
    db.session.add(new_entreprise)

    new_personnel=Personnel()
    new_personnel.per_nom="Grijol"
    new_personnel.per_mail="benjamin@trecobat.fr"
    new_personnel.per_prenom="Benjamin"
    new_personnel.per_entreprise=1
    db.session.add(new_personnel)

    new_stage=Stage()
    new_stage.sta_etudiant= 2
    new_stage.sta_duree=5
    new_stage.sta_annee_etudiant=1
    new_stage.sta_entreprise=1
    new_stage.sta_mission="développement web"
    new_stage.sta_tuteur=1
    new_stage.sta_ville="Lannilis"
    db.session.add(new_stage)
    db.session.commit()  # Sauvegarde les informations dans la base de donnees