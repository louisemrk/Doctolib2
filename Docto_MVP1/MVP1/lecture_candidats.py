import pandas
import json


'''def dataframe_exploitable(filename_clean,clefs_utiles):
    ce programme importe des donnees sous forme de fichier json qui sont à l'adresse filename_clean et renvoie un dataframe
    qui a pour colonnes des clefs utiles du tweet
    with open(filename_clean) as f:
        data = json.load(f)
        dictionnaire_utile=[]
        for candidat in data["Candidats"]:
            caract_nouveau_candidat={}
            for k in clefs_utiles:
                caract_nouveau_candidat[k]=candidat[k]
            dictionnaire_utile.append(caract_nouveau_candidat)
        donnees_exploitables=pandas.DataFrame(dictionnaire_utile)
        return donnees_exploitables'''


#data = dataframe_exploitable("candidats2.json",["first_name","last_name"])
#data.to_csv('candidats_dataframe.csv', sep = '\t', index = False)

with open("candidats2.json") as f:
            data = json.load(f)
            print(data["Candidats"][0]["first_name"])







