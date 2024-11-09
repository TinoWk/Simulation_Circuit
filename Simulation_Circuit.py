import math
import numpy as np
def resi_serie(tab):
    
    return sum(tab)

def resi_Parrallele(tab):
    retour=0.0    
    for i in range(len(tab)-1):
        if tab[i]!=0.0:
           retour+=1/tab[i]
        else:
            response=print("Nous avons rencontré une erreur de division par zéro!")
            break
    return 1/retour

def intensite(tension,resistance):
    try:
        return tension/resistance
    except ZeroDivisionError :
        print(" Erreur de division par Zéro!")
        


def puissance(tension, courant):
    return tension*courant

print(" Ce petit programme a pour but de :\n\n 1: Calculer la resistance equivalente des resitances montées en serie\n\n 2: Calculer la resistance equivlante des resistances monteés en parrllèle\n\n 3: Calculer l'intensité dans une branche à partir de la tension(ddp) et la resistance\n\n 4:Determiner la puissance  ")
choix=int(input("\n Que voudriez vous faire ? \n :"))
if choix==1:
    print(" Veuillez entrer leurs valeurs séparées par de virgules :")
    tab=(input().split(",") )
    tab=[float(val) for val in tab]
    print(" La résistance équivalente est R :",resi_serie(tab),"Ohm")
else :
    if choix==2:
         try :
              print(" Veuillez entrer leurs valeurs séparées par de virgules :")
              tab=(input().split(",") )
              tab=[float(val) for val in tab]
              print(" La résistance équivalente est R :",resi_Parrallele(tab),"Ohm")
         except ZeroDivisionError:
             print(" ")
    else:     
         if choix==3:
            tension=0.0
            resistance=0.0
            tension=float(input(" Veuillez entrer la tension :\n"))
            resistance=float(input(" Veuillez entrer la resistance:\n"))
            try :
                if intensite(tension,resistance)!= None :
                   print(" La valeur de l'Intensité est I :",intensite(tension,resistance)," A")
            except ZeroDivisionError:
                print()
         else :
             
            if choix==4:
               tension=0.0 
               courant=0.0
               tension=float(input(" Veuillez entrer la tension :\n"))
               courant=float(input(" Veuillez entrer le courant:\n"))
               print(" La valeur de la puissance  est P :",puissance(tension,courant)," Watt")
            else:
                 print(" Le choix est invalide, Reéssayez !")
