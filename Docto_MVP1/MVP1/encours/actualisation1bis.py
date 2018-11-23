import json


def code_html(filename_clean):
    '''ce programme prend des tweets en fichier json mal "indentés" localisé en filename et rajoute l'indentation
     pour avoir des "bons fichiers" json sur file_nameclean"'''

    with open("candidats1.json") as f:
            data = json.load(f)
    html = ""
    html=html+"f2 = open(filename_clean,"w")\n"
    html=html+"f2.write('<!DOCTYPE html>\n<html lang="fr">\n    <head>\n        <meta charset="utf-8"/>\n        <title>Acceuil</title>\n        <link rel="stylesheet" type="text/css" media="screen" href="style_candidat_internet1.css"/>\n    </head>\n')\n"
    html=html+"f2.write('    <body>\n')\n"
    html=html+"f2.write('        <header>\n            <h1>Liste des candidats</h1>\n            <hr>\n            <nav>\n                <a href="candidat_internet1.html" title="Accueil">Accueil</a>\n                <a href="candidate page.html" title="Nous contacter">Page candidat</a>\n            </nav>\n        </header>\n')\n"
    html=html+"f2.write('        <hr>\n        <p>\n')\n"
    html=html+"f2.write('            <table>\n                <thead>\n                    <tr>\n                        <th>Nom</th>\n                        <th>Prenom</th>\n                        <th>Page dediee</th>\n                    <tr>\n                </thead>\n                <tbody>\n')\n"

    html=html+"for candidat in data["Candidats"]:\n"
    html=html+"    f2.write('                    <tr>\n                        <td>'+candidat["first_name"]+'</td>\n                        <td>'+candidat["last_name"]+'</td>\n                        <td><a href="candidate page.html" title="la page de'+candidat["first_name"]+'">'+candidat["first_name"]+'</a></td>\n                    </tr>\n')\n"
    html=html+"f2.write('                </tbody>\n            </table>\n            <div class="separateur"></div>\n            <hr>\n        </p>\n    </body>\n</html>\n')\n"

#code_html("candidat_internet1.html")


