

f=open('p022_names.txt', 'r')#Ouverture du fichier contenant tous les noms
L=[] #Creation d'une liste vide que l'on va remplir au fur et à mesure par tous les noms.
for l in f: #On parcourt tous les lignes du fichier
    L+=l.split(',') #On coupe au niveau des virgules
f.close() #On ferme le fichier
#print(L)

print(L)

def score(nom): #création d'une fonction score pour le nom
    score=0 #On initialise le score à 0
    for i in nom: #On parcourt chaque élément de la chaîne de caractères
        score+=ord(i)-64 #la fonction ord renvoie le numéro de la lettre + 64 (après recherches sur internet sur comment trouver une fonction qui à un caractère associe un nombre
    return score  # On renvoie à la fin le score

def solve(): #Création d'une fonction visant à solutionner le problème 
    L.sort()  #On trie la liste des noms
    resultat=0 #On initialise le score à 0
    for i in range(len(L)): #On ceée une boucle for où l'on parcourt chaque élément 
        resultat+=score(i)*(i+1) #On ajoute au résultat son score en terme de nombre* sa position dans la liste
    return resultat #On renvoie le résultat final

solve()

#Le programme ne marche pas, j'ai des problèmes d'ordinateur. 

