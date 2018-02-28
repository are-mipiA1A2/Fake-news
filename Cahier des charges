                                                      CAHIER DES CHARGES


	Aujourd'hui, nous sommes confrontés à une globalisation des fausses informations. Face à ce phénomène, le président Macron a d'ailleurs annoncé un projet de loi punissant la diffusion de fausses informations. Notre génération étant particulièrement active sur les réseaux sociaux, nous avons choisi de mener cette étude pour les enjeux qu'elles présentent.  En effet, manipuler des personnes par le biais de l'information profère un intérêt économique et/ou politique non négligeable.
	Nous nous intéresserons donc ici aux fausses informations, appelées aussi « fake news ». Elles n'ont de nouveau que leur nom, puisqu'elles ont presque toujours existé. Cependant, l'avènement des réseaux sociaux et leur expansion planétaire ont fait exploser ce phénomène.

	Objectif : Modéliser la propagation des fake news dans une population en fonction de différents paramètres.

	Questions importantes autour du sujet :
- Que se passe-t-il lorsqu'on introduit une fausse information dans un environnement « connecté » ou non ?
- Qu'en est-il des personnes qui relaient délibérément une fausse information ?

	Phénomène d’étude :
	Le projet consiste en la modélisation de la diffusion de fake news dans une population de N individus ayant une opinion binaire initialisée à 0. 
- Les paramètres principaux qui entrent en jeu sont :
- Le nombre d’individus
- La fréquence d’exposition antérieure à ces fake news
- La crédibilité de la source d’informations
- La crédibilité de l’information
- Le nombre de réseaux sociaux sur lequel est inscrit un individu
- L'influence du voisinage

	Validation de l'étude :
	N'ayant pas accès à des données concrètes sur ce sujet, nous devons nous baser sur des prédictions empiriques pour identifier les facteurs qui influent positivement ou négativement sur la diffusion. Par exemple, nous pouvons intuiter qu'une information provenant d'une source sûre sera plus relayée. De plus, afin d'étayer nos résultats, nous pouvons analyser certaines fausses informations précédemment relayées pour tenter d'en estimer l'ampleur de propagation (en relevant par exemple le nombre de pays ou le nombre de sites dans lesquels l'information a été retransmise).
	Cependant, il faut préciser que ces analyses ne nous donneront qu'une idée. En effet, la propagation d'une fake news est difficilement quantifiable dans la mesure où ce n’est parfois qu'une parole, une discussion entre deux personnes.

	Ebauche de la modélisation :
Agents : les agents peuvent être des personnes ou des organismes médiatiques. Ceux-ci seront représentés en deux dimensions. On distinguera les agents neutres et les agents "malveillants" comme, par exemple, des organismes spécialisés dans la production de fausses informations.
Interactions : une information peut être transmise entre deux personnes qui discutent, entre deux personnes reliées par un réseau social ou entre un organisme médiatique (média audiovisuel, site Internet, journal, …) et une personne qui le consulte. Les agents pourront donc interagir directement (discussion entre deux agents s'ils sont humains) ou indirectement (diffusion par l'Internet ou relai par l'organisme médiatique). De plus, des interactions seront possibles entre personnes convaincues (PC), personnes non convaincues (PNC), organismes médiatiques (O).
	A la suite d'une interaction, plusieurs cas sont envisageables :
interaction PNC/PNC :
PNC + PNC = PNC + PNC
interaction PC/PC :
PC + PC = PC + PC
interaction PC/PNC :
PC + PNC = PC + PC
PC + PNC = PC + PNC
PC + PNC = PNC + PNC
interaction O/PC :
O + PC = O + PC
interaction O/PNC :
O + PNC = O + PC
O + PNC = O + PNC

	Répartition des tâches : (indicatif, très indicatif…)
	Nous établirons toutes les trois les grandes lignes du code. Puis, nous nous répartirons la modification du code en fonction des paramètres de la manière suivante :
Jenny : fréquence d'exposition antérieure
Ruxue : crédibilité de la source d'informations + crédibilité de l'information
Aya : nombre de réseaux sociaux sur lequel est inscrit de l'individu + influence du voisinage
