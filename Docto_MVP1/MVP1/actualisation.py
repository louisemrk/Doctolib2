import json


def code_html(filename_clean):
    '''ce programme prend des tweets en fichier json mal "indentés" localisé en filename et rajoute l'indentation
     pour avoir des "bons fichiers" json sur file_nameclean"'''

    with open("candidats2.json") as f:
            data = json.load(f)
    f2 = open(filename_clean,"w")
    f2.write("<table>\n  <thead>\n      <tr>\n        <th>Nom</th>\n        <th>Prenom</th>\n        <th>Page dediee</th>\n      <tr>\n  </thead>\n  <tbody>\n")

    for candidat in data["Candidats"]:
        f2.write("      <tr>\n        <td>"+candidat["first_name"]+"</td>\n        <td>"+candidat["last_name"]+"<td>\n        <td><a href=\"candidate_page.html\" title=\"la page de"+candidat["first_name"]+"\">"+candidat["first_name"]+"</a></td>\n      </tr>\n")
    f2.write("      </tbody>\n  <table>\n  <tbody>\n</table>\n")

code_html("candidat_internet.html")


