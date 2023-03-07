from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


def init_database():
    from database.models import Promotion, Etudiant, Taf
    db.drop_all()
    db.create_all()
    populate_database()

def populate_database():
    from database.models import Promotion, Role, Utilisateur, LienRoleUtilisateur, Etudiant, Taf,Stage, Entreprise, Personnel, Domaine, Enseignant, Ue, LienUeTaf

    Taf.ajouterTaf('DCL',"Developpement Collaboratif de Logiciels",1,1)

    Promotion.ajouterPromo(2024)
    Promotion.ajouterPromo(2025)

    Utilisateur.ajouterUtilisateur("admin","admin")

    Etudiant.ajouterEtudiant( "Pichereau","Hugo","hugo.pichereau@imt-atlantique.net","admin",2024)
    Etudiant.ajouterEtudiant("Vigouroux","Laure","laure.vigouroux@imt-atlantique.net","admin",2024)
    Etudiant.ajouterEtudiant("Robidou","Guillaume","guillaume.robidou@imt-atlantique.net","admin",2024)

    Entreprise.ajouterEntreprise("Trecobat")

    Personnel.ajouterPersonnel("Grijol","benjamin@trecobat.fr","Benjamin","Trecobat")

    Stage.ajouterStage("Trecobat","Grijol","développement web",5,"Lannilis")

    Enseignant.ajouterEnseignant("Le Calvar","Théo","theo.le-calvar@imt-atlantique.net","admin")
    Enseignant.ajouterEnseignant("Lèbre","Adrien","adrien.lebre@imt-atlantique.fr","admin")
    Enseignant.ajouterEnseignant("Südholt","Mario","mario.sudholt@imt-atlantique.fr","admin")
    Enseignant.ajouterEnseignant("Royer","Antoine","antoine.w.royer@gmail.com","admin")

    Ue.ajouterUe("WEBAPP","Découverte du développement web","Le Calvar")

    LienUeTaf.ajouterLienUeTaf("WEBAPP","DCL")

    Domaine.ajouterDomaine("Informatique")

    Role.ajouterRole("admin")

    LienRoleUtilisateur.ajouterRoleUtilisateur("admin","admin")