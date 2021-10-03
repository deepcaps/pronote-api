pronote-api
==========
### Unofficial pronote API
[![PYTHON](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://html.com/)
[![FLASK](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![HEROKU](https://img.shields.io/badge/Heroku-430098?style=flat&logo=heroku&logoColor=white)](https://heroku.com/)



# How to use ?

## On your app
Vous devez juste envoyer une requete sur le serveur `https://deepcaps-pronote-api.herokuapp.com/`

![mainhtml](./images/mainhtml.png)

Si tout les arguments son entrés correctements, le serveur enverra une réponse au bout de **~20 secondes** en format `JSON` ...

![json](./images/json.png)

... sinon une erreur de type `Internal serveur error: 500` ou `null` sera renvoyée

![500error](./images/500error.png)

### Example of request
> Vous devez remplacer les variables ici entre crochets **<>** par les elements demandés (ex.: *username=\<username\>* ==> *username=usernamepronote*)

Pour avoir la moyenne de chaque matière: `http://deepcaps-pronote-api.herokuapp.com/matter_moyenne?username=<username>&password=<password>&link=<link>`

Pour avoir la moyenne de l'élève: `http://deepcaps-pronote-api.herokuapp.com/student_moyenne?username=<username>&password=<password>&link=<link>`

Pour avoir la moyenne de la classe: `http://deepcaps-pronote-api.herokuapp.com/classroom_moyenne?username=<username>&password=<password>&link=<link>`

Les infos supplementaires sur les requetes sont ici : `https://deepcaps-pronote-api.herokuapp.com/`

## Local
pass ==> installation locale


# A savoir
pass ==> données de connection non enregistrer, librairies,...


# Me contacter
pass ==> me contacter adresse mail


# Infos
[![MAINTENED](https://img.shields.io/badge/maintained-yes-green.svg)](https://github.com/deepcaps/pronote-api/)
[![WEBSITE](https://img.shields.io/website-up-down-green-red/https/deepcaps-pronote-api.herokuapp.com)](https://deepcaps-pronote-api.herokuapp.com/)
