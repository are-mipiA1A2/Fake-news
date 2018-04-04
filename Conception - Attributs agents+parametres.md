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
|N      |int    |None         |à définir        |Oui        |Nb d'individus|
|news   |float  |[0,1]        |à définir        |Oui        |Crédibilité de la news : crédible si tend vers 1|
|malv   |int    |range(N)     |à définir        |Oui        |Degré de malveillance de l'envt : compte le nb d'agents malveillants|
|sigma  |float  |[0,1]        |à définir        |Oui        |Seuil de persuasion : val d'écart minimale entre 2 p, ou 1 p et une moyenne de p, pour modifier la conviction|
|co     |float  |[0,selon nb réseaux]|à définir |Oui        |Connectivité du milieu : nb de réseaux sociaux moyen par individu|

## Liste des expériences :

Pourcentage de personnes qui croient au bout certains étapes
-en fonction de Crédibilité de la news
-en fonction de Degré de malveillance de l'envt 
-en fonction de Seuil de persuasion

la moyenne des p en fonction de:
-en fonction de Crédibilité de la news
-en fonction de Degré de malveillance de l'envt 
-en fonction de Seuil de persuasion

Ecart-type des p en fonction de:
-en fonction de Crédibilité de la news
-en fonction de Degré de malveillance de l'envt 
-en fonction de Seuil de persuasion
