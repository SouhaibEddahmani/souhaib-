class produit:
    def __init__(self,nom,prix,quantite_stock):
        self.nom = nom
        self.prix = prix
        self.quantite_stock = quantite_stock

    def afficher_details(self):
       print(f"nom:{self.nom}")
       print(f"prix:{self.prix}")
       print(f"quantite_stock:{self.quantite_stock}")

p1 = produit("malak","5000","5")
p1.afficher_details()



class produit:
    def __init__(self,nom,prix,quantite_stock):
        self.__nom = nom
        self.__prix = prix
        self.__quantite_stock = quantite_stock
    def get_nom(self):
        return self.__nom
    def set_nom(self,nouveau_nom):
        self.__nom = nouveau_nom
    def get_prix(self):
        return self.__prix
    def set_nom(self,nouveau_prix):
        self.__prix = nouveau_prix
    def get__quantite_stock(self):
        return self.__quantite_stock
    def set_quantite_stock(self,nouveau_quantite_stock):
        self.__quantite_stock = nouveau_quantite_stock


p1 = produit("tablet", 1000, 20)
p1.afficher_details()
p2 = produit("flormar", 1000, 20)
p2.afficher_details()
produit.N_produit()


class produit:
    def __init__(self, nom, prix, quantite_stock):
        self.nom = nom
        self.prix = prix
        self.quantite_stock = quantite_stock

class aliment(produit):

    def _init_(self,date_peremption,nom,prix,quantite_stock):
        super()._init_(nom,prix,quantite_stock)
        self.date_peremption = date_peremption
    @staticmethod
    def sortlist(list):
        for i in range(len(list) - 1):
            nombremax= i
            for j in range(i + 1, len(list)):
                if list[j] > list[nombremax]:
                    nombremax = j
            if nombremax != i:
                list[i], list[nombremax] = list[nombremax], list[i]
        return list

    list = [17, 65, 81]
    print(list)
    l2 = sortlist(list)
    print(l2)

    @staticmethod
    def printstar(n):
        for i in range(n+1):
            for j in range(i):
                print("*",end="")
            print("")

    n= 5
    n2 = printstar(n)
print(n2)
