def solve(n): 
    ch=str(n) #création d'une chaine de caractères composée du nombre
    b=0 #initialisation de la variable
    for k in ch: #On parcourt chaque élément de la chaine
        b+=int(k) #On convertit chaque élément en entier et on le somme à b 
    return(b)  #La fonction renvoie la somme


def solve2(n): 
    r=0 #Deuxième façon de résoudre le problème. On initialise une variable à 0
    while n!=0: #Le principe consiste à diviser eculidiennement par 10 successivement jusqu'à ce que le reste soit nul
        r+=n%10 #On récupère à chaque le chiffre des unités du nombre. Ex 459: on ajoute 9 à r
        n=n//10 #On divise de façon euclidienne. Ex 459: 45. Losrqu'on obtient 0 on a bien effectué la somme de tous les nombres. 
    return(r) # On renvoie la somme de tous les chiffres du nombre. 



 # D'un point de vue rigoureux, la deuxième méthode est plus mathématique.  

    
        
