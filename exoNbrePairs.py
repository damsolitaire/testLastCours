#trouver la somme des nombres pair d'une lliste donnée

def sumNbrePairs(liste):
    sum = 0
    for nbre in liste:
        if nbre % 2 == 0:  
            sum += nbre 
    return sum

liste = [52, 93, 27, 658, 4, 1, 74, 19, 365, 73, 8, 82, 94, 6, 2]
resultat = sumNbrePairs(liste)
print(resultat)