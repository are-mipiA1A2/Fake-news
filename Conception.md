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
- valeur de "connexion" du média en fonction de son type (ex: valeur d'un site Internet > valeur d'un journal)

**__Procédures__**

- création de la fake news
- prise de décision (changement d'opinion ou non)
- diffusion par l'agent s'il est convaincu

 ### Interactions
 Nous distinguerons 2 types d'interactions : discussion physique et consultation à distance. Ces 2 types engendreront des influences différentes sur la prise de décision :
 
 1. Discussion physique :
 - influence du pouvoir de persuasion accrue
 - influence de l'opinion (sois convaincu et tu convaincras les autres...)
 - influence de la crédibilité de la news elle-même
 
 2. Consultation à distance :
 - influence de la crédibilité de la news
 - influence de la fréquece d'exposition antérieure à la même news








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

