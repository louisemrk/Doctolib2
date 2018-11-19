import pandas
import json


def dataframe_exploitable(filename_clean,clefs_utiles):
    '''ce programme importe des donnees sous forme de fichier json qui sont à l'adresse filename_clean et renvoie un dataframe
    qui a pour colonnes des clefs uriles du tweet'''
    with open(filename_clean) as f:
        data = json.load(f)
        dictionnaire_utile=[]
        for candidat in data["Candidats"]:
            caract_nouveau_tweet={}
            for k in clefs_utiles:
                if k != "len":
                    caract_nouveau_tweet[k]=tweet[k]
            dictionnaire_utile.append(caract_nouveau_tweet)
        donnees_exploitables=pandas.DataFrame(dictionnaire_utile)
        return donnees_exploitables


data = dataframe_exploitable("candidat.json",["nom","prénom"])

