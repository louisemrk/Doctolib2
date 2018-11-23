from flask import Flask
import json
app = Flask(__name__, static_url_path="/static")


def code_html():
    '''ce programme ouvre le fichier json candidatsmvp3 et renvoie une chaîne de caractères qui correspond à la page d'accueil'''

    with open("candidatsmvp3.json") as f:
            data = json.load(f)

    out = ''
    out = out + '<!DOCTYPE html>\n<html lang="fr">\n    <head>\n        <meta charset="utf-8"/>\n        <title>Acceuil</title>\n        <link rel="stylesheet" type="text/css" media="screen" href="static/style_index.css"/>\n    </head>\n'
    out = out + '    <body>\n'
    out = out + '        <header>\n            <h1>Liste des candidats</h1>\n            <hr>\n            <nav>\n                <a href="/0" title="Accueil">Accueil</a>\n                            </nav>\n        </header>\n'
    out = out + '        <hr>\n        <p>\n'
    out = out + '            <table>\n                <thead>\n                    <tr>\n                        <th>Nom</th>\n                        <th>Prénom</th>\n                        <th>Page dédiée</th>\n                    <tr>\n                </thead>\n                <tbody>\n'

    for candidat in data["Candidats"]:
        out = out + '                    <tr>\n                        <td>'+candidat["last_name"]+'</td>\n                        <td>'+candidat["first_name"]+'</td>\n                        <td><a href="http://127.0.0.1:5000/'+str(candidat["Id"])+'" title="la page de'+candidat["first_name"]+'">'+candidat["first_name"]+'</a></td>\n                    </tr>\n'
    out = out + '                </tbody>\n            </table>\n            <div class="separateur"></div>\n            <hr>\n        </p>\n    </body>\n</html>\n'
    return out


def html_candidat(candidat):
    '''prend en paramètre "candidat" :une chaine de caractère qui correspond à l'id d'un candidat et renvoit une chaîne de caractère correspondant à un la page html correspondant au candidat '''


    out = ''
    out = out + '<!DOCTYPE html>\n<html lang="fr">\n    <head>\n        <meta charset="utf-8"/>\n        <title>Acceuil</title>\n        <link rel="stylesheet" type="text/css" media="screen" href="static/style_page_candidat.css"/>\n    </head>\n'
    out = out + '    <body>\n'
    out = out + '        <header>\n            <h1>Candidat '+ candidat["Id"]+'</h1>\n            <hr>\n            <nav>\n                <a href="../0" title="Accueil">Accueil</a>\n                            </nav>\n        </header>\n'
    out = out + '        <hr>\n        <p>\n'
    out = out + '            <h2>Nom</h2>\n            <em>'+candidat["last_name"]+'</em>\n            <h2>Prénom</h2>\n            <em>'+candidat["first_name"]+'</em>\n            <h2>Date de naissance</h2>\n            <em>'+candidat["date_birth"]+'</em>\n            <h2>Date de l'+str("'")+'interview</h2>\n            <em>'+candidat["interview_date"]+'</em>\n            <h2>Ville de naissance</h2>\n            <em>'+candidat["birth_city"]+'</em>\n'
    out = out + '            <div class="separateur"></div>\n            <h2>Données</h2>\n'
    out = out + '            <table>\n                <thead>\n                    <tr>\n                        <th>Nombre de fonctions</th>\n                        <th>Nombre de commentaires</th>\n                        <th>Qualité de variable</th>\n                        <th>Niveau</th>\n'
    out = out + '                <tbody>\n                    <tr>\n                        <td>'+candidat["fichiers"][0]["stats"]["functionsCount"]+'</td>\n                        <td>'+candidat["fichiers"][0]["stats"]["commentCount"]+'</td>\n                        <td>'+candidat["fichiers"][0]["stats"]["variableNameQuality"]+'</td>\n                        <td>'+candidat["metrics"]["level"]+'</td>\n                    <tr>\n                </tbody>\n            </table>\n'
    out = out + '            <div class="separateur"></div>\n            <hr>\n            </p>\n            <a href="../0">Revenir à la page acceuil</a>\n      </body>\n</html>\n        <tr>\n        </thead>\n'
    return out


def candidates (path_file):
    '''cette fonction retourne une chaine de caractère correspondant au fichier à l'adresse " path_file"'''
    with open (path_file, "r") as file:
        data=json.load(file)

    return data

@app.route('/<qwer>')
def page_candidat(qwer):
    '''génère les pages webs_ qwer est une chaine de caractère correspondant à l'index d'une pages'''

    candidate=candidates("candidatsmvp3.json")
    if qwer=="0":
        return code_html()
    else:
        for person in candidate["Candidats"]:
            if person["Id"]==qwer:
                return html_candidat(person)
        return "Page not found"


