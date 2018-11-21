from flask import Flask


#si on transformele fichier .json a .txt (je vais chercher comme travailler directemment au json)
def web_personne(path_file):
    with open ("path file", "r") as file:
        candidates=file.readlines
        for candidate in candidates:
            app = Flask(candidate[0])
            @app.route('/'+'candidate[0]'+"." + "candidate[1]')

