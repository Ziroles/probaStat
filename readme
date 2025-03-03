olist_orders_dataset.csv => Date de livraison estimé vs reelle (en jours)
olist_order_items_dataset.csv => prix livraison
olist_order_payments_dataset.csv => payment_sequential nb de paiement par commande 
olist_order_reviews_dataset.csv => Review
olist_sellers_dataset.csv => vendeur

Pour population, voir : https://datacommons.org/place/country/BRA?category=Demographics

# Consigne

Un seul livrable est attendu par binôme, sous la forme d'un rapport écrit présentant votre capacité à mettre en œuvre vos compétences en statistique (descriptive et inférentielle abordées en cours). L'évaluation portera en particulier sur les compétences suivantes, issues de la présentation de ce cours :
● calculer et interpréter les principaux paramètres de position et de dispersion dans une distribution de données à un caractère. Comparer plusieurs distributions ;
● estimer une moyenne ou une proportion par intervalle de confiance, comparer 2 moyennes ou proportions par intervalle de confiance ;
● savoir réaliser et interpréter un test statistique.
 
Concrètement : il s'agit pour vous de présenter, sous forme graphique dès que cela est possible, des caractéristiques de statistique descriptive (et pas seulement des moyennes arithmétiques...) et de réaliser des estimations de moyennes sur des échantillons que vous aurez sélectionnés (pour éventuellement les comparer aux données réelles des populations disponibles).
Il vous est demandé d'analyser au moins 4 caractères (cf. CM n° 04) issus du jeu de données en passant par une représentation graphique, présentant au moins 3 types de caractéristiques différents (cf. CM n° 05), via au moins 2 types de diagrammes différents (cf. CM n° 04). Rappel : une taille est un exemple de caractère, alors qu'une moyenne est un exemple de caractéristique.
Il faudra aussi réaliser au moins deux estimations par intervalles de confiance différents, présentant chacune un risque α propre (cf. cours à venir).
 
Des pistes vous seront données en séance si vous ne voyez pas comment mettre en valeur vos acquisitions de ces différentes compétences, et par conséquent, quoi mettre dans vos rapports. L'idée principale est de montrer vos capacités à savoir à la fois mettre en forme et analyser des données statistiques réelles, pour en tirer des conclusions, qui pourraient intéresser votre hiérarchie. Quoi qu'il en soit, il sera de votre ressort de trouver comment traduire cela sous forme de scripts en Python.
Il n'est pas prévu d'effectuer de revue de code et vous n'aurez pas à joindre vos scripts au rapport.

# Proposition :

# 1. Calculer et interpréter les principaux paramètres de position et de dispersion


## Caractères analysés :

Prix des produits
Frais de livraison
Temps de livraison (temps entre commande et livraison)
Notes des clients
## Représentation graphique :

Boxplots pour visualiser la dispersion des données et identifier les valeurs aberrantes.
Histogrammes pour montrer la distribution des prix, des frais de livraison et des notes des clients.
## Statistiques calculées :

Moyenne, médiane, mode
Écart-type, variance
Intervalle interquartile
Comparaison entre les catégories de produits pour voir lesquelles ont la plus grande dispersion de prix.
## Exploitation :

Comparer la distribution des prix des différentes catégories pour identifier les écarts significatifs.
Identifier les produits avec des prix aberrants (outliers) et proposer des recommandations.
Comparer la dispersion des délais de livraison entre les États pour détecter des zones avec des retards fréquents.

# 2. Estimation par intervalle de confiance de moyennes ou proportions


## Intervalles de confiance sur :

La moyenne du prix des produits (intervalle de confiance à 95%)
Le taux de clients satisfaits (proportion des notes ≥ 4 étoiles)
## Représentation graphique :

Barres d'erreur pour visualiser l'intervalle de confiance autour des moyennes.
## Comparaison des intervalles de confiance :

Comparaison des prix entre différentes catégories de produits.
Comparaison des délais de livraison moyens entre deux États avec un intervalle de confiance à 90% et un autre à 95%.

# 3. Réalisation et interprétation d'un test statistique
Propositions :

## Tests possibles :

Test de comparaison de moyennes (Test t de Student) : Comparer le prix moyen entre deux catégories de produits.
Test du Khi² : Vérifier si la distribution des notes clients dépend significativement de la catégorie de produit.
Test de proportion : Comparer le pourcentage de livraisons en retard entre deux États.
## Représentation graphique :

Violin plot ou KDE plot pour visualiser la distribution des prix avant le test de Student.
Tableaux croisés et heatmaps pour explorer la dépendance entre les notes et la catégorie de produit avant d’appliquer le test du Khi².