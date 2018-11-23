import json
import numpy.random as rd

def date_entretien():
    '''retourne une date d'entretient aléatoire (chaine de caractère)'''
    j=rd.randint(0,30,1)
    m=rd.randint(0,12,1)
    an=rd.randint(2010,2018,1)
    date=str(j[0])+'/'+str(m[0])+'/'+str(an[0])
    return(str(date))

def date_naissance():
    '''renvoie une date de naissance aléatoire (chaine de caractère)'''
    j=rd.randint(0,30,1)
    m=rd.randint(0,12,1)
    an=rd.randint(1991,1981,1)
    date=str(j[0])+'/'+str(m[0])+'/'+str(an[0])

def modif_json():
    '''renvoit un fichier json "candidatmvp2.json" qui ajoute au fichier json "candidats.json" : Id, lieu de l'entretien, date de l«,entretien, date de naissance. '''
    with open('candidats.json') as f:

        data=json.load(f)
        with open('candidatsmvp2.json','w')as f2:
            f2.write('{\n    "Candidats" :[ \n')
            id_n=0
            n=len(data['Candidats'])-1
            k=0
            for candidat in data['Candidats']:
                    print(k)
                    candidat["interview_date"]=date_entretien()
                    m=candidat['first_name'][0]
                    id_n=id_n+1
                    id=m+str(id_n)
                    candidat['Id']=id+'"'
                    f2.write('      { \n')
                    n2=len(candidat)-1
                    i=0
                    for element in candidat:
                        if i==0:
                            f2.write('         "'+str(element)+'"'+":"+'"'+str(candidat[element])+'",\n')
                        elif i!=n2:

                            f2.write('       "'+str(element)+'"'+":"+'"'+str(candidat[element])+'",\n')

                        else :
                            if k!=n:
                                f2.write('       "'+str(element)+'"'+":"+'"'+str(candidat[element])+"\n       },\n")

                            else :
                                f2.write('       "'+str(element)+'"'+":"+'"'+str(candidat[element])+"\n       }\n")
                                print('good')

                        i=i+1
                    k=k+1
            f2.write('\n    ]\n}')








