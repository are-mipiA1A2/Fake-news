# Conception
## Attributs des agents
### _Etres humains_

|Nom    |Type   |Intervalle     |Valeur initiale  | Fixe ?    |Explication|
|:-----:|:-----:|:-------------:|:---------------:|:---------:|:---------:|
|nom    |str    |[str(0),str(N)]|str(k)           |Oui        |Nom : nom de l'agent (clé du dict)|
|op     |int    |{0,1}          |0                |Non        |Opinion : y croit (1) ou non (0)|
|deja_vu|int    |[0,steps]      |0                |Non        |Déjà vu : nombre d'expositions à l'information par le biais de quelqu'un qui y croit|
|fp     |float  |[0,1]          |Random           |Oui        |Force de persuasion : capacité à convaincre quelqu'un (accrue qd tend vers 1)|
|p      |float  |[0,1]          |0.5              |Non        |Conviction : caractérise la conviction à la news (tend vers 1) ou non (tend vers 0). Si assez élevée, fait basculer l'opinion de 0 à 1 et inversement|

### _Organismes médiatiques_
|Nom    |Type   |Intervalle               |Valeur initiale  | Fixe ?    |Explication|
|:-----:|:-----:|:-----------------------:|:---------------:|:---------:|:---------:|
|nom    |str    |['OM'+str(0),'OM'+str(N)]|'OM'+str(k)      |Oui        |Nom : nom de l'organisme (clé du dict)|
|op     |int    |{0,1}                    |0                |Non        |Opinion : ne relaie l'info que s'il l'estime correcte (1)|
|deja_vu|int    |[0,steps]                |0                |Non        |Déjà vu : nombre d'expositions à l'info par le biais de quelqu'un qui y croit|
|fp     |float  |[0,1]                    |Random mais >0.7 |Oui        |Force de persuasion : accrue car organisme médiatique|
|p      |float  |[0,1]                    |0.5              |Non        |Conviction : |

### _Organismes médiatiques malveillants_
|Nom    |Type   |Intervalle               |Valeur initiale  | Fixe ?    |Explication|
|:-----:|:-----:|:-----------------------:|:---------------:|:---------:|:---------:|
|nom    |str    |['XOM'+str(0),'XOM'+str(N)]|'XOM'+str(k)   |Oui        |Nom : nom de l'organisme (clé du dict)|
|op     |int    |{0,1}                    |0                |Non        |Opinion : relaie l'info même si n'y croit|
|deja_vu|int    |[0,steps]                |0                |Non        |Déjà vu : nombre d'expositions à l'info par le biais de quelqu'un qui y croit|
|fp     |float  |[0,1]                    |Random mais >0.7 |Oui        |Force de persuasion : accrue car organisme médiatique|
|p      |float  |[0,1]                    |0.75             |Oui        |Conviction : toujours à 0.75 car cherche à garder le p des autres au dessus de 0.5|

## Paramètres du modèle :

|Nom    |Type   |Intervalle   |Valeur initiale  | Fixe ?    |Explication|
|:-----:|:-----:|:-----------:|:---------------:|:---------:|:---------:|
|news   |float  |[0,1]        |à entrer        |Oui        |Crédibilité de la news : crédible si tend vers 1|
|malv   |float  |[0,1]        |à entrer        |Oui        |Degré de malveillance de l'environnement : proportion d'agents malveillants parmi les médias|
|co     |int    |range(11)    |à entrer        |Oui        |Connectivité du milieu : nombre de réseaux sociaux moyen par individu|

## Indicateurs :

|Nom    |Type   |Intervalle   |Explication
|:-----:|:-----:|:-----------:|:---------:|
|MOY    |float  |[0,1]        |Moyenne des convictions de tous les agents à la fin d'une simulation|
|TA     |float  |[0,100]      |Taux d'adoption : pourcentage d'opinions à 1 à la din d'une simulation|
|TPS    |int    |range(steps) |Temps d'adotpion : nombre d'étapes qu'il faut pour que le pourcentage d'opinions à 1 soit au moins égal à 90%|

## Liste des expériences :  

Ci-dessous la liste des expériences qui nous ont semblé les plus pertinentes.  

**MOY** en fonction de **news**

**TA** en fonction de **news**

**TPS** en fonction de **co**  
**TPS** en fonction de **malv**


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
