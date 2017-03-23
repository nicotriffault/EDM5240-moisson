### MES COMMENTAIRES ET CORRECTIONS SONT MARQUÉS PAR TROIS DIÈSES

### Bonne idée!
### Je comprends les pépins que tu as eus.
### Ils exigent qu'on utilise des fonctions plus avancées de BeautifulSoup,
### fonctions auxquelles j'ai eu rarement recours, et que je n'ai donc pas eu le temps de vous montrer.
### Voici tout de même comment s'y prendre, dans ce cas-ci

#coding: utf-8

# Mon but est de lister les délégués commerciaux canadiens (affiliés au ministère des Affaires étrangères) dans un csv.

# j'importe les modules dont j'aurai besoin

import csv
import requests
from bs4 import BeautifulSoup

#j'ajoute l'url d'où je veux extraire des infos. J'ai d'abord voulu faire tous les pays du monde, mais c'était long. À des fins pratiques, je me suis concentré sur les pays d'Amérique du Sud.  

### J'essaie avec tous les pays du monde
url = "http://deleguescommerciaux.gc.ca/trade-commissioner-delegue-commercial/results-resultats.aspx?cids=AF&cids=ZA&cids=AL&cids=DZ&cids=DE&cids=AD&cids=AO&cids=AI&cids=AG&cids=AN&cids=SA&cids=AR&cids=AM&cids=AW&cids=AU&cids=AT&cids=AZ&cids=BS&cids=BH&cids=BD&cids=BB&cids=BY&cids=BE&cids=BZ&cids=BJ&cids=BM&cids=BT&cids=BO&cids=BA&cids=BW&cids=BR&cids=BN&cids=BG&cids=BF&cids=BI&cids=KH&cids=CM&cids=CV&cids=CL&cids=CN&cids=CY&cids=PS&cids=CO&cids=KM&cids=CD&cids=CG&cids=KR&cids=KP&cids=CR&cids=CI&cids=HR&cids=CU&cids=DK&cids=DJ&cids=DM&cids=EG&cids=SV&cids=AE&cids=EC&cids=ER&cids=ES&cids=EE&cids=US&cids=ET&cids=FJ&cids=FI&cids=FR&cids=GA&cids=GM&cids=GE&cids=GH&cids=GI&cids=GR&cids=GD&cids=GL&cids=GP&cids=GU&cids=GT&cids=GN&cids=GQ&cids=GW&cids=GY&cids=GF&cids=HT&cids=HN&cids=HK&cids=HU&cids=NF&cids=KY&cids=CK&cids=FK&cids=FO&cids=MP&cids=MH&cids=SB&cids=TC&cids=VI&cids=VG&cids=WF&cids=IN&cids=ID&cids=IR&cids=IQ&cids=IE&cids=IS&cids=IL&cids=IT&cids=JM&cids=JP&cids=JO&cids=KZ&cids=KE&cids=KI&cids=XK&cids=KW&cids=LA&cids=LS&cids=LV&cids=LB&cids=LR&cids=LY&cids=LI&cids=LT&cids=LU&cids=MO&cids=MG&cids=MY&cids=MW&cids=MV&cids=ML&cids=MT&cids=MA&cids=MQ&cids=MU&cids=MR&cids=MX&cids=FM&cids=MD&cids=MC&cids=MN&cids=ME&cids=MS&cids=MZ&cids=MM&cids=NA&cids=NR&cids=NP&cids=NI&cids=NE&cids=NG&cids=NU&cids=NO&cids=NC&cids=NZ&cids=OM&cids=UG&cids=UZ&cids=PK&cids=PW&cids=PA&cids=PG&cids=PY&cids=NL&cids=PE&cids=PH&cids=PN&cids=PL&cids=PF&cids=PR&cids=PT&cids=QA&cids=CF&cids=MK&cids=TL&cids=DO&cids=KG&cids=SK&cids=CZ&cids=RE&cids=RO&cids=UK&cids=RU&cids=RW&cids=KN&cids=LC&cids=SM&cids=PM&cids=VA&cids=VC&cids=WS&cids=AS&cids=ST&cids=SN&cids=RS&cids=SC&cids=SL&cids=SG&cids=SI&cids=SO&cids=SD&cids=SS&cids=LK&cids=SE&cids=CH&cids=SR&cids=SZ&cids=SY&cids=TJ&cids=TW&cids=TZ&cids=TD&cids=TH&cids=TG&cids=TK&cids=TO&cids=TT&cids=TN&cids=TM&cids=TR&cids=TV&cids=UA&cids=EU&cids=UY&cids=VU&cids=VE&cids=VN&cids=YE&cids=ZM&cids=ZW&search=+Soumettre+&lang=fra"

# url = "http://deleguescommerciaux.gc.ca/trade-commissioner-delegue-commercial/results-resultats.aspx?cids=AR&cids=BO&cids=BR&cids=CL&cids=CO&cids=EC&cids=GY&cids=GF&cids=PY&cids=PE&cids=SR&cids=UY&cids=VE&search=+Soumettre+&lang=fra"

# Je me présente au site

entetes = {
    "User-Agent":"Nicolas Triffault - Étudiant en journalisme à l'UQAM",
    "From":"nicolastriffault@gmail.com"
}

# J'indique à mon script quoi faire avec la page web désignée et avec BS4

contenu = requests.get(url, headers=entetes)

page = BeautifulSoup(contenu.text, "html.parser")

# je donne un nom au fichier csv que je vais créer

fichier = "delegues-commerciaux-JHR.csv" ### Je rebaptise le nom du fichier pour le distinguer

# J'ai été trouver les infos que je veux (pays, domaines d'expertise des délégués, noms des délégués) dans le code html de la page.

# d = page.find("div", class_="span-6").find_all

# print(len(d))

# if d.next_element == h2:
#     print(d.next_element)

### Je commence par recueillir les noms de tous les pays
### Je les place dans une variable «touspays»

touspays = page.find("div", class_="span-6").find_all("h2")

### Je procède un pays à la fois
for pays in touspays:
    print(pays.text) ### Affichage du nom du pays aux fins de vérification

### Je cherche le nom du pays dans toute la page
### Et quand je le trouve, je crée une liste de tous les éléments HTML qui suivent (next_siblings)
    for element in page.find("h2", string=pays.text).next_siblings:
        # print(element.name)

### J'examine chacun de ces éléments HTML
### Tant que l'élément n'est pas un <h2>, ce qui voudrait dire que je suis rendu au pays suivant, j'examine l'élément
        if element.name != "h2":

### Si l'élément est un <h3>, c'est que je suis arrivé à une catégorie
            if element.name == "h3":
                categorie = element.text
                # print(categorie)

### Si l'élément est un <div>, c'est que je suis arrivé à un.e délégué.e
            elif element.name == "div":
                nomDelegue = element.a.text
                delegueURL = "http://deleguescommerciaux.gc.ca/trade-commissioner-delegue-commercial/" + element.a["href"]

### J'en profite pour aller chercher plus d'infos sur la page de ce.tte délégué.e
### En fait, je vais seulement recueillir son courriel
                c = requests.get(delegueURL, headers=entetes)
                pageDelegue = BeautifulSoup(c.text, "html.parser")
                for lien in pageDelegue.find_all("a"):
                    if "mailto:" in lien["href"]:
                        # print(lien.text)

### C'est ici qu'on peut écrire toute l'info sur le.la délégué.e qu'on vient d'identifier
                        delegue = [pays.text,categorie,nomDelegue,lien.text]
                        print(delegue)
                        nelson = open(fichier,"a")
                        mandela = csv.writer(nelson)
                        mandela.writerow(delegue)
        else:
            break

#     for pays2 in page.find("div", class_="span-6").find_all("h2"):
#         if pays1 == pays2
#             print(pays2.text)
#             print(page.h3)

# for pays in page.find("div", class_="span-6").find_all("h2"):
#     pays2 = pays.text
    
#     for domaines in page.find("div", class_="span-6").find_all("h3"):
#         domaines2 = domaines.text

#         for noms in page.find("div", class_="span-6").find_all("div", class_="margin-left-xsmall"):
#             noms2 = noms.find("a", class_="ui-link").text
    
#     # Je réunis mes variables
    
#             valeurs = pays2, domaines2, noms2
            
#     # Je crée un fichier csv contenant ces dites variables
            
#             with open("delegues-commerciaux.csv", "a") as csv_file:
#                     csv_delegues = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC) 
#                     csv_delegues.writerow(valeurs)
                    
# # Malheureusement, le script écrit toutes les possibilités de combinaisons de pays/domaines/noms. Le fichier csv a donc un demi-million de lignes plutôt qu'environ 200. Je n'arrive pas à régler ce problème. 
# # J'ai tenté de réunir mes variables dans un seul "for ___ in ___", sans succès, puisque j'avais des erreurs du types "AttributeError: 'ResultSet' object has no attribute 'text'".
    
# # for item in page.find("div", class_="span-6"):
# #     pays = item.find_all("h2")
# #     domaines = item.find_all("h3").text
# #     noms = item.find_all("div", class_="margin-left-xsmall").find("a", class_="ui-link").text
# #     valeurs = pays, domaines, noms
            
# # J'avais préalablement essayer d'aller chercher les variables en utilisant les url proposées en cliquant sur le nom des délégués(en codant les lignes suivantes). J'ai abandonné parce que leurs domaines d'expertise ne sont pas indiqués sur ces pages, uniquement dans la page "d'accueil" où les délégués sont listés. 

# # for delegues in page.find("div", class_="span-6").find_all("div", class_="margin-left-xsmall"):
#     # debut = "http://deleguescommerciaux.gc.ca/trade-commissioner-delegue-commercial/"
#     # lien = debut + delegues.a["href"]
#     # contenu2 = requests.get(lien, headers=entetes)
#     # page2 = BeautifulSoup(contenu2.text,"html.parser")
    
# # Je suis bien triste d'avoir au final un csv qui ne veut rien dire, surtout au regard des heures passées à travailler dessus. Il est 22h30 lundi soir, je m'avoue vaincu.
# # Au moins, le script fonctionne et j'ai les variables qui m'intéressent. C'est la disposition dans le fichier csv qui n'est pas au rdv...
