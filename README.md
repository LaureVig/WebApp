
# Développement web avec Flask 
# Cahier des charges 

## Objectif du module
Être capable de réaliser rapidement en binôme un SI de type Web en utilisant un framework Web Python. 

## Prérequis
Bases de la programmation en Python.

## Introduction
Flask est un framework de développement Web permettant l’écriture d’applications Web en Python. Il est possible de l’utiliser pour écrire des systèmes d’information qui favorisent l’interaction avec les utilisateurs en leur permettant de saisir de l’information, en affichant des pages Web contenant des données et en stockant les informations dans des bases de données relationnelles. Flask est un framework accessible qui permet d’aborder la conception de systèmes d’information avec des étudiants qui ont de bonnes bases en programmation avec Python.

L’objectif de ce rattrapage est de vérifier votre bonne compréhension des technologies et les enjeux rencontrés dans la conception de systèmes d’informations de type application web.Vous pourrez vous appuyer sur les supports fournis lors de l’UE ou disponibles sur le web en grande quantité. 

## Travail demandé
IMTA Alumni
Le sujet proposé cette année est de mettre en œuvre un système d’informations permettant de gérer un annuaire des anciens élèves et diplômés de l’école. 
L’application sera organisée autour de deux profils : administrateur et utilisateur. 
L’administrateur devra être en mesure de créer : 
- Créer/modifier/supprimer des promotions
- Créer/modifier/supprimer des étudiants
- Créer/modifier/supprimer des TAFs
- Créer/modifier/supprimer des entreprises 

Les utilisateurs (i.e. les étudiants)  devront être en mesure de venir renseigner/modifier : 
- Leur état civil
- les TAF qu’il/elle aura suivi lors de son parcours 
- les informations relatives à son projet de fin d'étude (titre du sujet/résumé du projet de fin d’étude et éventuellement le rapport de stage)
- l’entreprise dans lequel il a fait son stage 
- les coordonnées de son tuteur. Si l’entreprise n’existe pas dans le système, il devra être en mesure de la créer (vous prendrez le soin d'éviter la création de doublons en retournant les noms d’entreprises qui se rapprochent de la syntaxe donnée par l’étudiant : exemple Dassault vs dassault systèmes).
- Leur position actuelle (ingénieur, chef de projet, etc. dans telle entreprise). 

Pour les deux profils, un tableau de bord indiquera le nombre de fiches étudiants dans le système d’informations, et le nombre d’entreprises. Via ce même tableau de bord, l’administrateur ou les utilisateurs devront pouvoir faire des recherches spécifiques, comme par exemple : 
- Lister l’ensemble des étudiants d’une promotion donnée,
- Lister l’ensemble des étudiants ayant fait un stage dans une entreprise
- Lister l’ensemble des étudiants d’une même TAF sur une période spécifique (par exemple l’ensemble des étudiants qui a suivi la TAF DCL de 2020 à 2023)
etc.

D’une manière générale, les fonctionnalités évoquées ici sont minimalistes, vous pouvez bien évidemment proposer des améliorations comme par exemple la recherche d’informations dans les rapports de stage déposés. 

PS: Un très bon projet est un projet qui serait utilisable par un autre étudiant de l’école (i.e. qui n’aurait pas suivi le module).


# TODO
- finir les fonctions d'update
- finir les fonctions de tri et filtrage
- créer un getbyid pour chaque (pour sélectionner dans le front)