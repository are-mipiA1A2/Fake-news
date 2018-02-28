# Conception

## Système

### Agents
Les agents sont :
- des individus
- des organismes médiatiques

**__Attributs__**

1. Des individus :
- opinion (binaire, initialisée à 0)
- crédulité
- pouvoir de persuasion
- nombre de réseaux sociaux sur lesquels est inscrit l'individu
- degré de malveillance

2. Des organismes médiatiques :
- opinion
- pouvoir de persuasion
- degré de malveillance

**__Procédures__**

- création de la fake news
- prise de décision (changement d'opinion ou non)
- diffusion par l'agent s'il est convaincu
 ### 

Les différents agents sont:
 - une population de N individus, modelisée par une matrice;
 - une source d'informations, modelisée par un entier qui prend la valeur 0 ou 1;
 - une entreprise spécialiée dans la production de fausses informations, modélisée par un entier qui prend la valeur 0 ou  1
 
 
Attributs:
    opinion, initialisée à 0
    nombre de réseau sociaux sur lequel est inscrit l'individu
    seuil de confiance en la source
    fréquence d'exposition antérieure aux fausses informations
    âge
    force de persuasion de la source
    
Paramètres:
    influence de la source d'information
    intensité de la fausse information
    
Un individu i appartenant à N a dans son voisinage un autre individu j appartenant à N. 
  Le but serait d'incrémenter un à un les paramètres ainsi que les attributs de i et d'observer si 


On pourra lorsque on change la valeur d'un des attributs, la stocker dans une variable.

