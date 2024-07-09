from src.vent import *
p=client("saidouchrif","nnsdnsnd",19,1,"JJODZJ")
p1=client("said","nnsdnsnd",19,1,"JJODZJ")
p3=client("hamza","nnsdnsnd",19,1,"JJODZJ")
"""import csv
f=open("client.csv","w")
e=csv.writer(f,delimiter=",")
e.writerow(["Nom complete","CIN","age","id client","Budget"])
e.writerow([p.nom_complet,p.CIN,p.age,p.id_client,p.Budget])
"""

""" 2 import csv
boncommend=[{"Nom complete":p.nom_complet,"CIN":p.CIN,"age":p.age,"id client":p.id_client,"Budget":p.Budget},
            {"Nom complete":p1.nom_complet,"CIN":p1.CIN,"age":p1.age,"id client":p1.id_client,"Budget":p1.Budget},
            {"Nom complete":p3.nom_complet,"CIN":p3.CIN,"age":p3.age,"id client":p3.id_client,"Budget":p3.Budget},
            ]
f=open("client.csv","w")
e=csv.DictWriter(f,delimiter=";",fieldnames=boncommend[0].keys())
e.writeheader()
for ligne in boncommend:
    e.writerow(ligne)
f.close()"""
""" 1 import csv
boncommend=[p.__dict__,p1.__dict__]
f=open("client.csv","w")
e=csv.DictWriter(f,delimiter=";",fieldnames=boncommend[0    ].keys())
e.writeheader()
for ligne in boncommend:
    e.writerow(ligne)
f.close()"""