

from database.database import db

#DIS-MOI QUE CA MARCHE STP !!!
class Etudiant(db.Model):
    etu_id = db.Column(db.Integer, primary_key=True)
    etu_nom = db.Column(db.Text, nullable=False)
    etu_prenom = db.Column(db.Text, nullable=False)
    etu_mail = db.Column(db.Text, nullable=False)
    etu_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateur.uti_id'))
    etu_position_id = db.Column(db.Integer, db.ForeignKey('position.pos_id'))
    etu_promotion_id = db.Column(db.Integer, db.ForeignKey('promotion.pro_annee'))
    etu_taf1 = db.Column(db.Integer, db.ForeignKey('taf.taf_id'))
    etu_taf2 = db.Column(db.Integer, db.ForeignKey('taf.taf_id'))
    etu_stage2= db.Column(db.Integer, db.ForeignKey('stage.sta_id'))
    etu_stage1 = db.Column(db.Integer, db.ForeignKey('stage.sta_id'))
    etu_stage3 = db.Column(db.Integer, db.ForeignKey('stage.sta_id'))

    def __repr__(self):
        return '<Etudiant {}>'.format(self.etu_nom)

    def ajouterEtudiant(nom:str,prenom:str,mail:str,login:str,promo:int,position:str="null",taf_id1="null",taf_id2="null",stage1="null",stage2="null",stage3="null"):
        new_student = Etudiant()
        new_student.etu_nom=nom
        new_student.etu_prenom=prenom
        new_student.etu_mail=mail
        new_student.etu_utilisateur=db.session.query(Utilisateur).filter(Utilisateur.uti_login==login).first().uti_id
        print(position)
        if position!="null":
            new_student.etu_position_id=db.session.query(Position).filter(Position.pos_id==position).first().pos_id
        else :
            new_student.etu_position_id="NULL"
        new_student.etu_promotion_id=db.session.query(Promotion).filter(Promotion.pro_annee==promo).first().pro_annee
        new_student.etu_taf1=taf_id1
        new_student.etu_taf2=taf_id2
        new_student.etu_stage1=stage1
        new_student.etu_stage2=stage2
        new_student.etu_stage3=stage3
        db.session.add(new_student)
        db.session.commit()


    def get_etudiants_par_promo(annee:int):
        return db.session.query(Etudiant).join(Promotion).filter(Promotion.pro_annee==annee).all()

    def get_etudiants_par_taf(taf_id:int):
        return "Pas encore implémenté"

    def supprimerEtudiant(id:int):
        Etudiant.get_by_id(id)
        db.session.delete(etudiant)

    def get_etudiants_par(colonne:str,searchfield:any):
        if colonne=='etu_nom':
            return db.session.query(Etudiant).filter(Etudiant.etu_nom==searchfield).all()
        elif colonne=='etu_prenom':
            return db.session.query(Etudiant).filter(Etudiant.etu_prenom == searchfield).all()
        elif colonne=='etu_mail':
            return db.session.query(Etudiant).filter(Etudiant.etu_mail == searchfield).all()
        elif colonne =='etu_promotion_id':
            return db.session.query(Etudiant).filter(Etudiant.etu_promotion_id == searchfield).all()

    def sort_etudiants_par(colonne:str):
        liste_etudiants = db.session.query(Etudiant).all()
        liste_noms = []
        if colonne=='etu_nom':
            for etudiant in liste_etudiants:
                if etudiant.etu_nom not in liste_noms :
                    liste_noms.append(etudiant.etu_nom)
                liste_noms.sort()
        elif colonne=='etu_prenom':
            for etudiant in liste_etudiants:
                if etudiant.etu_prenom not in liste_noms :
                    liste_noms.append(etudiant.etu_prenom)
                liste_noms.sort()
        elif colonne=='etu_mail':
            for etudiant in liste_etudiants:
                if etudiant.etu_mail not in liste_noms :
                    liste_noms.append(etudiant.etu_mail)
                liste_noms.sort()
        liste_resultat = []
        for etudiant in liste_noms :
            for i in range(len(Etudiant.get_etudiants_par(colonne,etudiant))):
                liste_resultat.append(Etudiant.get_etudiants_par(colonne,etudiant)[i])
        return liste_resultat

    def get_by_id(id:int):
        return db.session.query(Etudiant).filter(Etudiant.etu_id == id).first()

    def modifierEtudiant(self,nom="null",prenom="null",mail="null",login:str="null",promo:int="null",position:str="null",taf_id1="null",taf_id2="null",stage1="null",stage2="null",stage3="null"):
        if nom!="null":
            self.etu_nom=nom
        if prenom!="null":
            self.etu_prenom=prenom
        if mail!="null":
            self.etu_mail=mail
        if login!="null":
            self.etu_utilisateur=db.session.query(Utilisateur).filter(Utilisateur.uti_login==login).first().uti_id
        if position!="null":
            self.etu_position_id=db.session.query(Position).filter(Position.pos_id==position).first().pos_id
        if promo!="null":
            self.etu_promotion_id=db.session.query(Promotion).filter(Promotion.pro_annee==promo).first().pro_annee
        if taf_id1!="null":
            self.etu_taf1=taf_id1
        if taf_id2!="null":
            self.etu_taf2=taf_id2
        if stage1!="null":
            self.etu_stage1=stage1
        if stage2!="null":
            self.etu_stage2=stage2
        if stage3!="null":
            self.etu_stage3=stage3
        db.session.add(self)
        db.session.commit()

class Promotion(db.Model):
    pro_annee = db.Column(db.Integer, nullable=False,  primary_key=True)
    pro_promotion = db.relationship('Etudiant', backref='promotion')

    def ajouterPromo(annee:int):
        new_promo=Promotion()
        new_promo.pro_annee=annee
        db.session.add(new_promo)
        db.session.commit()

    def supprimerPromo(id: int):
        promo = db.session.query(Promotion).filter(Promotion.pro_id == id).first()
        db.session.delete(promo)

    def modifierPromotion(self,annee="null"):
        if annee!="null":
            self.pro_annee=annee
        db.session.add(self)
        db.session.commit()

    def getAllPromotion():
        return db.session.query(Promotion).all()
    def get_by_id(id: int):
        return db.session.query(Promotion).filter(Promotion.pro_annee == id).first()

    def __repr__(self):
        return '<Promotion {}>'.format(self.pro_annee)


class Taf(db.Model):
    taf_id = db.Column(db.Integer, primary_key=True)
    taf_nom = db.Column(db.Text, nullable=False)
    taf_description = db.Column(db.Text, nullable=False)
    taf_responsable_id = db.Column(db.Integer, db.ForeignKey('enseignant.ens_id'), nullable=False)
    taf_domaine_id = db.Column(db.Integer, db.ForeignKey('domaine.dom_id'), nullable=False)
    taf_lien_ue = db.relationship('LienUeTaf', backref='taf')

    def __repr__(self):
        return 'TAF {}'.format(self.taf_nom)

    def ajouterTaf(nom:str,description:str,respo:int,domaine:int):
        new_taf=Taf()
        new_taf.taf_nom=nom
        new_taf.taf_description=description
        new_taf.taf_responsable_id = respo
        new_taf.taf_domaine_id = domaine
        db.session.add(new_taf)
        db.session.commit()

    def supprimerTaf(id:int):
        taf = db.session.query(Taf).filter(Taf.taf_id==id).first()
        db.session.delete(taf)

    def getAllTaf():
        return db.session.query(Taf).all()

    def modifierTaf(self,nom="null",description="null",respo="null",domaine="null"):
        if nom!="null":
            self.taf_nom=nom
        if description!="null":
            self.taf_description=description
        if respo!="null":
            self.taf_responsable_id = respo
        if domaine!="null":
            self.taf_domaine_id = domaine
        db.session.add(self)
        db.session.commit()

    def get_by_id(id: int):
        return db.session.query(Taf).filter(Taf.taf_id == id).first()
class Enseignant(db.Model):
    ens_id = db.Column(db.Integer, primary_key=True)
    ens_nom = db.Column(db.Text, nullable=False)
    ens_prenom = db.Column(db.Text, nullable=False)
    ens_mail = db.Column(db.Text, nullable=False)
    ens_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateur.uti_id'))

    def ajouterEnseignant(nom:str,prenom:str,mail:str,login:str):
        new_ens=Enseignant()
        new_ens.ens_nom=nom
        new_ens.ens_prenom=prenom
        new_ens.ens_mail=mail
        new_ens.ens_utilisateur= db.session.query(Utilisateur).filter(Utilisateur.uti_login==login).first().uti_id
        db.session.add(new_ens)
        db.session.commit()

    def supprimerEnseignant(id:int):
        ens = db.session.query(Enseignant).filter(Enseignant.ens_id==id).first()
        db.session.delete(ens)

    def modifierEnseignant(self,nom:str,prenom:str,mail:str,login:str):
        if nom != "null":
            self.ens_nom=nom
        if prenom != "null":
            self.ens_prenom=prenom
        if mail != "null":
            self.ens_mail=mail
        if login != "null":
            self.ens_utilisateur= db.session.query(Utilisateur).filter(Utilisateur.uti_login==login).first().uti_id
        db.session.add(self)
        db.session.commit()

    def getAllEnseignant():
        return db.session.query(Enseignant).all()

    def __repr__(self):
        return '<Enseignant {}>'.format(self.ens_nom)

class Domaine(db.Model):
    dom_id = db.Column(db.Integer, primary_key=True)
    dom_nom = db.Column(db.Text, nullable=False)

    def ajouterDomaine(nom:str):
        new_dom=Domaine()
        new_dom.dom_nom=nom
        db.session.add(new_dom)
        db.session.commit()

    def supprimerDomaine(id:int):
        domaine= db.session.query(Domaine).filter(Domaine.dom_id==id).first()
        db.session.delete(domaine)

    def modifierDomaine(self,nom="null"):
        if nom!="null":
            self.dom_nom=nom
        db.session.add(self)
        db.session.commit()

    def getAllDomaine():
        return db.session.query(Domaine).all()
    def __repr__(self):
        return '<Domaine {}>'.format(self.dom_nom)

class Stage(db.Model):
    sta_id = db.Column(db.Integer, primary_key=True)
    sta_entreprise = db.Column(db.Integer, db.ForeignKey('entreprise.ent_id'))
    sta_tuteur = db.Column(db.Integer, db.ForeignKey('personnel.per_id'))
    sta_mission = db.Column(db.Text)
    sta_duree = db.Column(db.Integer)
    sta_ville = db.Column(db.Text)

    def ajouterStage(entreprise:str,tuteur:str,mission:str,duree:int,ville:str):
        new_stage=Stage()
        new_stage.sta_entreprise=db.session.query(Entreprise).filter(Entreprise.ent_nom==entreprise).first().ent_id
        new_stage.sta_tuteur=db.session.query(Personnel).filter(Personnel.per_nom==tuteur).first().per_id
        new_stage.sta_mission=mission
        new_stage.sta_duree=duree
        new_stage.sta_ville=ville
        db.session.add(new_stage)
        db.session.commit()

    def supprimerStage(id:int):
        stage = db.session.query(Stage).filter(Stage.sta_id==id).first()
        db.session.delete(stage)

    def modifierStage(self,entreprise="null",tuteur="null",mission="null",duree="null",ville="null"):
        if entreprise!= "null":
            self.sta_entreprise=db.session.query(Entreprise).filter(Entreprise.ent_nom==entreprise).first().ent_id
        if tuteur != "null":
            self.sta_tuteur=db.session.query(Personnel).filter(Personnel.per_nom==tuteur).first().per_id
        if mission != "null":
            self.sta_mission=mission
        if duree != "null":
            self.sta_duree=duree
        if ville != "null":
            self.sta_ville=ville
        db.session.add(self)
        db.session.commit()

    def get_by_id(id: int):
        return db.session.query(Stage).filter(Stage.sta_id == id).first()

    def getAllStage():
        return db.session.query(Stage).all()

class Ue(db.Model):
    ue_id = db.Column(db.Integer, primary_key=True)
    ue_nom = db.Column(db.Text)
    ue_description = db.Column(db.Text)
    ue_responsable_id = db.Column(db.Integer, db.ForeignKey('enseignant.ens_id'), nullable=False)

    def ajouterUe(nom:str,desription:str,respo:str):
        new_ue=Ue()
        new_ue.ue_nom=nom
        new_ue.ue_description=desription
        new_ue.ue_responsable_id=db.session.query(Enseignant).filter(Enseignant.ens_nom==respo).first().ens_id
        db.session.add(new_ue)
        db.session.commit()

    def supprimerUe(id:int):
        ue = db.session.query(Ue).filter(Ue.ue_id==id).first()
        db.session.delete(ue)

    def modifierUe(self,nom="null",desription="null",respo="null"):
        if nom!= "null":
            self.ue_nom=nom
        if description != "null":
            self.ue_description=desription
        if respo != "null":
            self.ue_responsable_id=db.session.query(Enseignant).filter(Enseignant.ens_nom==respo).first().ens_id
        db.session.add(self)
        db.session.commit()

    def getAllUe():
        return db.session.query(Ue).all()

class LienUeTaf(db.Model):
    lut_ue_id = db.Column(db.Integer, db.ForeignKey('ue.ue_id'), primary_key=True)
    lut_taf_id = db.Column(db.Integer, db.ForeignKey('taf.taf_id'), primary_key=True)

    def ajouterLienUeTaf(ue,taf):
        new_lien = LienUeTaf()
        new_lien.lut_taf_id=db.session.query(Taf).filter(Taf.taf_nom==taf).first().taf_id
        new_lien.lut_ue_id=db.session.query(Ue).filter(Ue.ue_nom==ue).first().ue_id
        db.session.add(new_lien)
        db.session.commit()

class Entreprise(db.Model):
    ent_id =db.Column(db.Integer, primary_key=True)
    ent_nom = db.Column(db.Text)

    def ajouterEntreprise(nom:str):
        new_ent=Entreprise()
        new_ent.ent_nom=nom
        db.session.add(new_ent)
        db.session.commit()

    def supprimerEntreprise(id:int):
        entreprise = db.session.query(Entreprise).filter(Entreprise.ent_id==id).first()
        db.session.delete(entreprise)

    def modifierEntreprise(self,nom:str):
        if nom != "null":
            self.ent_nom=nom
        db.session.add(self)
        db.session.commit()

    def getAllEntreprise():
        return db.session.query(Entreprise).all()


class Personnel(db.Model):
    per_id = db.Column(db.Integer, primary_key=True)
    per_nom =db.Column(db.Text)
    per_prenom =db.Column(db.Text)
    per_mail =db.Column(db.Text)
    per_entreprise = db.Column(db.Integer, db.ForeignKey('entreprise.ent_id'))

    def ajouterPersonnel(nom:str,prenom:str,mail:str,entreprise:str):
        new_personnel=Personnel()
        new_personnel.per_nom=nom
        new_personnel.per_prenom=prenom
        new_personnel.per_mail=mail
        new_personnel.per_entreprise=db.session.query(Entreprise).filter(Entreprise.ent_nom==entreprise).first().ent_id
        db.session.add(new_personnel)
        db.session.commit()

    def supprimerPersonnel(id:int):
        perso = db.session.query(Personnel).filter(Personnel.per_id==id).first()
        db.session.delete(perso)

    def modifierPersonnel(self,nom:str="null",prenom:str="null",mail:str="null",entreprise:str="null"):
        if nom != "null":
            self.per_nom=nom
        if prenom != "null":
            self.per_prenom=prenom
        if mail != "null":
            self.per_mail=mail
        if entreprise != "null":
            self.per_entreprise=db.session.query(Entreprise).filter(Entreprise.ent_nom==entreprise).first().ent_id
        db.session.add(self)
        db.session.commit()

    def getAllPersonnem():
        return db.session.query(Personnel).all()

class LienRoleUtilisateur(db.Model):
    lru_role = db.Column(db.Integer, db.ForeignKey('role.rol_id'), primary_key=True)
    lru_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateur.uti_id'), primary_key=True)

    def ajouterRoleUtilisateur(role:str,utilisateur:str):
        new_lien=LienRoleUtilisateur()
        new_lien.lru_role=db.session.query(Role).filter(Role.rol_nom==role).first().rol_id
        new_lien.lru_utilisateur=db.session.query(Utilisateur).filter(Utilisateur.uti_login==utilisateur).first().uti_id
        db.session.add(new_lien)
        db.session.commit()

class Role(db.Model):
    rol_id = db.Column(db.Integer,  primary_key=True)
    rol_nom = db.Column(db.Text)

    def ajouterRole(nom:str):
        new_role=Role()
        new_role.rol_nom=nom
        db.session.add(new_role)
        db.session.commit()

    def supprimerRole(id:int):
        role = db.session.query(Role).filter(Role.rol_id==id).first()
        db.session.delete(role)

    def modifierRole(self,nom ="null"):
        if nom != "null":
            self.rol_nom=nom
            db.session.add(self)
            db.session.commit()

class Utilisateur(db.Model):
    uti_id = db.Column(db.Integer, primary_key=True)
    uti_login = db.Column(db.Text)
    uti_mdp = db.Column(db.Text)

    def ajouterUtilisateur(login:str,mdp:str):
        new_user=Utilisateur()
        new_user.uti_login=login
        new_user.uti_mdp=mdp
        db.session.add(new_user)
        db.session.commit()

    def supprimerUtilisateur(id:int):
        user = db.session.query(Utilisateur).filter(Utilisateur.uti_id==id).first()
        db.session.delete(user)

    def modifierUtilisateur(self,login="null",mdp="null"):
         if login!="null":
            self.uti_login = login
         if mdp != "null":
            self.uti_mdp = mdp
         db.session.add(self)
         db.session.commit()

class Position(db.Model):
    pos_id = db.Column(db.Integer, primary_key=True)
    pos_nom = db.Column(db.Text)
    pos_entreprise = db.Column(db.Integer, db.ForeignKey('entreprise.ent_id'))

    def ajouterPosition(nom:str,entreprise:str):
        new_pos=Position()
        new_pos.pos_nom=nom
        new_pos.pos_entreprise= db.session.query(Entreprise).filter(Entreprise.ent_nom==entreprise).first().ent_id
        db.session.add(new_pos)
        db.session.commit()

    def supprimerPosition(id:int):
        position = db.session.query(Position).filter(Position.pos_id==id).first()
        db.session.delete(position)

    def modifierPosition(self,nom:str="null",entreprise:str="null"):
        if nom != "null":
            self.pos_nom=nom
        if entreprise != "null":
            self.pos_entreprise= db.session.query(Entreprise).filter(Entreprise.ent_nom==entreprise).first().ent_id
        db.session.add(self)
        db.session.commit()

    def getAllPosition():
        return db.session.query(Position).all()

    def get_by_id(id: int):
        return db.session.query(Position).filter(Position.pos_id == id).first()