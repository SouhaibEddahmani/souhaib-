from abc import ABC,abstractmethod
class vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass
    @abstractmethod
    def prime(n):
        c=0
        for x in range(2,n//2):
            if n % x ==0:
                c+=1
        if c==0:
            print("premier")
        else:
            print("non premier")

class voiture(vehicule):
    @abstractmethod
    def deplacer(self):
        print("le type de vehicule est:voiture")
class avion(vehicule):
    @abstractmethod
    def deplacer(self):
        print("le type de vehicule est:avion")
vehicule.prime(17)

v2=voiture.prime(37)

from abc import ABC,abstractmethod
class forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass

class rectangle(forme):
    def __init__(self,longeur,largeur):
        super().__init__()
        self.longeur = longeur
        self.largeur = largeur
    def calculer_surface(self):
        return self.longeur*self.largeur
    @staticmethod
    def somme_aires(r1,r2):
        return r1.calculer_surface() + r2.calculer_surface()
import math
class cercle(forme):
    def __init__(self,rayon):
        super().__init__()
        self.rayon = rayon
    def calculer_surface(self):
        return math.pi * self.rayon**2
    def somme_aires(self,c2):
        return self.calculer_surface()+c2.calculer_surface()
    def __add__(self, x):
        return self.calculer_surface()+ x .calculer_surface()

r1 = rectangle(9,4)
print(r1.calculer_surface())
r2 = cercle(8)
print(r2.calculer_surface())
print(r1.somme_aires(r1,r2))


