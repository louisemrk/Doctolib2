import json
import numpy.random as rd

def dateentretien():
    with open('candidats.json') as f:
        data=json.load(f)
        dic={}
        for candidat in data['Candidats']:
            j=rd.randint(0,30,1)
            m=rd.randint(0,12,1)
            an=rd.randint(2010,2018,1)
            candidat["Date de l'entretien"]=str(str(j)+'/'+str(m)+'/'+str(an))
        return data
print(dateentretien())
