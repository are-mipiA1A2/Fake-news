# Conception
## Attributs des agents
### _Etres humains_

|Nom    |Type   |Intervalle     |Valeur initiale  | Fixe ?    |Explication|
|:-----:|:-----:|:-------------:|:---------------:|:---------:|:---------:|
|nom    |str    |[str(0),str(N)]|str(k)           |Oui        |Nom : nom de l'agent (clé du dict)|
|op     |int    |{0,1}          |0                |Non        |Opinion : y croit (1) ou non (0)|
|deja_vu|bool   |[True,False]   |False            |Non        |Déjà vu : a déjà été confronté à la news (True) ou pas (False)|
|fp     |float  |[0,1]          |Random           |Oui        |Force de persuasion : capacité à convaincre qqun (accrue qd tend vers 1)|
|p      |float  |[0,1]          |0.5              |Non        |Conviction : caractérise la conviction à la news (tend vers 1) ou non (tend vers 0). Si assez élevée, fait basculer l'opinion de 0 à 1 et inversement|

### _Organismes médiatiques_
|Nom    |Type   |Intervalle               |Valeur initiale  | Fixe ?    |Explication|
|:-----:|:-----:|:-----------------------:|:---------------:|:---------:|:---------:|
|nom    |str    |['OM'+str(0),'OM'+str(N)]|'OM'+str(k)      |Oui        |Nom : nom de l'organisme (clé du dict)|
|op     |int    |{0,1}                    |0                |Oui        |Opinion : relaie une info ssi il l'estime correcte (1)|
|deja_vu|bool   |[True,False]             |False            |Non        |Déjà vu : a déjà été confronté à la news (True) ou pas (False)|
|fp     |float  |[0,1]                    |Random mais >0.7 |Oui        |Force de persuasion : accrue car organisme médiatique|
|p      |float  |[0,1]                    |0.5              |Oui        |Conviction : 0.5 car neutre|

## Paramètres du modèle :

|Nom    |Type   |Intervalle   |Valeur initiale  | Fixe ?    |Explication|
|:-----:|:-----:|:-----------:|:---------------:|:---------:|:---------:|
|N      |int    |None         |à définir        |Oui        |Nombre d'individus|
|news   |float  |[0,1]        |à définir        |Oui        |Crédibilité de la news : crédible si tend vers 1|
|malv   |int    |range(N)     |à définir        |Oui        |Degré de malveillance de l'environnement : pourcentage d'agents malveillants dans l'envt|
|sigma  |float  |[0,1]        |à définir        |Oui        |Seuil de persuasion : val d'écart minimale entre 2 p, ou 1 p et une moyenne de p, pour modifier la conviction|
|co     |float  |[0,selon nb réseaux]|à définir |Oui        |Connectivité du milieu : nombre de réseaux sociaux moyen par individu|

## Liste des expériences :

**Pourcentage de personnes qui croient au bout certains étapes** en fonction:  
-de la Crédibilité de la news  
-du Degré de malveillance de l'envt  
-du Seuil de persuasion  

**la moyenne des p** en fonction de:  
-de la Crédibilité de la news  
-du Degré de malveillance de l'envt  
-du Seuil de persuasion  

**Ecart-type des p** en fonction de:  
-de la Crédibilité de la news  
-du Degré de malveillance de l'envt  
-du Seuil de persuasion  


## Liste des agents   

### _Etres humains_   
* Rôle: Mettre en évidence l'influence d'une news sur ses attributs propres      
* Actions: 
   - Je participe à la discussion physique et à distance   
   - Je relaie l'information si et seulement si j'y croit   
   - J'écoute les autres: je suis convaincu (ou pas) par les autres selon leur forces de persuasion   
* Attributs caractéristiques:   
   - Opinion binaire   
   - deja_vu (nombre de fois qu'il a vu l'information)   
   - Force de persuasion     
   - Conviction   
                                
### _Organismes médiatiques neutres_   
* Rôle: Diffuser la news    
* Actions:  
   - Je participe à la discussion physique et à distance   
   - Je relaie l'information si j'y croit   
   - Je démentis l'information si je ne croît pas l'information   
* Attributs caractéristiques: 
   - Opinion binaire   
   - deja_vu (nombre de fois qu'il a vu l'information)   
   - Force de persuasion ( compris entre 0.7 et 1)      
   - Conviction (>0.5) 

   
### _Organismes médiatiques malveillants_   
* Rôle: Diffuser une fake news en sachant qu'elle est fausse    
* Actions:  
   - Je participe à la discussion physique et à distance   
   - Je relaie l'information même si je ne la croît pas   
* Attributs caractéristiques: 
   - Opinion 1   
   - deja_vu (nombre de fois qu'il a vu l'information)   
   - Force de persuasion ( compris entre 0.7 et 1)      
   - Conviction (>0.5)   
   
## Liste des environnements   
### _Discussion physique_
* Caractéristiques:
   - Matrice carrée de taille N_1dim
   - Réseau discussion representé par un dictionnaire qui associe à chaque individu un tuple, de la forme   
      dict[str:tuple[int,bool,float,float]]
   
### _Reseaux Sociaux_   
