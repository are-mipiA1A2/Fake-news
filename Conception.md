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

 ### Interaction
 Nous distinguerons 2 types d'interactions : discussion physique et consultation à distance. A la suite de l'interaction, une prise de décision sera effectuée. Cependant, le type d'interaction influera sur la prise de décision de la manière suivante :
 
 1. Discussion physique :
 - influence du pouvoir de persuasion accrue
 - influence de l'opinion (sois convaincu et tu convaincras les autres...)
 - influence de la crédibilité de la news elle-même
 - influence du voisinage
 
 2. Consultation à distance :
 - influence de la crédibilité de la news
 - influence de la fréquece d'exposition antérieure à la même news
 - influence du voisinage

## Environnement
L'environnement **global** sera constitué de plusieurs réseaux représentés par des graphes (listes ou des listes de dictionnaires). Il y aura des réseaux sociaux et un réseau physique (de discussion). Ces réseaux constitueront la possibilité d'interaction entre 2 agents.  
L'environnement **local**, lui, correspond au voisinage.

**__Variables :__**  
- nombre de réseaux (caractérise le degré de connexion du milieu)
