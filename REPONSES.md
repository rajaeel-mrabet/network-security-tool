# Réponses — TP 1 : Premiers pas avec Git et GitHub

## Question 1 : Quelle est la différence entre `git add` et `git commit` ?

La commande `git add` permet de sélectionner les fichiers ou les modifications que l'on souhaite inclure dans le prochain commit. La commande `git commit` enregistre ces modifications dans l'historique local du dépôt Git avec un message descriptif.

## Question 2 : Que représente un commit dans Git ?

Un commit est un instantané de l'état des fichiers suivis par Git à un moment donné. Il permet de conserver l'historique des modifications, de retrouver une version précédente et de comprendre l'évolution du projet.

## Question 3 : Pourquoi créer une branche plutôt que modifier directement la branche principale ?

Une branche permet de développer une fonctionnalité indépendamment de la branche principale `main`. Cela facilite les tests, limite les risques de perturber le code stable et permet d'examiner les modifications avant leur fusion.

## Question 4 : Quel est le rôle d'une Pull Request dans un projet collaboratif ?

Une Pull Request permet de proposer l'intégration des modifications d'une branche dans une autre branche. Elle permet aux membres de l'équipe d'examiner le code, de discuter des changements et de vérifier leur qualité avant la fusion.