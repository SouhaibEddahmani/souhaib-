#QCM:
# 1-a
# 2-b
# 3-c
# 4-a
# 5-b
# 6-a
#ex1
from abc import ABC,abstractmethod
class Personne(ABC):
    def __init__(self,nom_complet,CIN,age):
        self.nom_complet=nom_complet
        self.CIN=CIN
        self.age=age
    @abstractmethod
    def afficher_detail(self):
        print(f"{self.nom_complet}")
        print(f"{self.CIN}")
        print(f"{self.age}")
    @staticmethod
    def prime(a, b):
        l = []
        for i in range(a, b + 1):
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    break
                else:
                    l.append(i)
                    break
        return l

#ex2
class client(Personne):
    n=0
    def __init__(self,nom_complet,CIN,age,id_client,Budget):
        super().__init__(nom_complet,CIN,age)
        self.id_client=id_client
        self.Budget=Budget
        client.n+=1
        """ adilsqsqsdqd"""
    def __str__(self):
        return f"{self.nom_complet},{self.age}"
    def __sub__(self, other):
        return self.age-other.age
    def afficher_detail(self):
        print(f"{self.id_client}")
        print(f"{self.CIN}")
        print(f"{self.nom_complet}")
        print(f"{self.age}")
        print(f"{self.Budget}")
    def __add__(self,tr):
        return self.Budget+ tr.Budget
    @classmethod
    def nombre_total(cls):
        print(f"{cls.n}")
    @staticmethod
    def etoile(n):
        for i in range(n, 0, -1):
            print("*" * i)
#ex3
class Vendeur(Personne) :
    n = 0
    def __init__(self,nom_complet,CIN,age,id_client,Budget,id_vendeur,salaire):
        super().__init__(nom_complet, CIN, age)
        self.id_client=id_client
        self.Budget=Budget
        self.id_vendeur=id_vendeur
        self.__salaire=salaire
        Vendeur.n+=1


    def afficher_detail(self):
        print(f"{self.id_client}")
        print(f"{self.CIN}")
        print(f"{self.nom_complet}")
        print(f"{self.age}")
        print(f"{self.Budget}")
        print(f"{self.id_vendeur}")

    def get_salaire(self):
        return self.__salaire

    def set_salaire(self, nouveau_salaire):
        self.__salaire = nouveau_salaire

    @classmethod
    def nombre_total(cls):
        print(f"{cls.n}")

#ex4
class Produit:
    n = 0
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
        Produit.n +=1

    def Afficher_detail(self):
        print(f"Nom: {self.nom}, Prix: {self.prix}")

    @classmethod
    def nombre_total(cls):
        print(f"{cls.n}")

    @staticmethod
    def sort(l):
        p = []
        while l != []:
            p.append(min(l))
            l.remove(min(l))
        for x in p:
            if x not in l:
                l.append(x)
        return l
#ex5
class Vente:
    n = 0
    def __init__(self, id_vente, date_vente, vendeur, client, produits):
        self.id_vente = id_vente
        self.date_vente = date_vente
        self.vendeur = vendeur
        self.client = client
        self.produits = produits
        self.prix_total_vente = sum([x.prix for x in produits])
        Vente.n+=1

    def Afficher_detail(self):
        print(f"ID vente: {self.id_vente}, Date vente: {self.date_vente}, Vendeur: {self.vendeur.nom} {self.vendeur.prenom}, Client: {self.client.nom} {self.client.prenom}, Produits: {[p.nom for p in self.produits]}, Prix total vente: {self.prix_total_vente}")

    @classmethod
    def nombre_total(cls):
        print(f"{cls.n}")

    @staticmethod
    def meilleure_vente(ventes):
        max_prix = max([v.prix_total_vente for v in ventes])
        meilleure_vente = [v for v in ventes if v.prix_total_vente == max_prix]
        meilleure_vente.Afficher_detail()

#partie_test





