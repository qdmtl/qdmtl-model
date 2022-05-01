# qdmtl-ontology

Ce dépôt contient les sources de l’ontologie développée dans le cadre du [projet `QDMTL`](https://qdmtl.ca). Ce projet soutient la préparation et la publication d’un jeu de données ouvertes et liées (LOD) sur les quartiers disparus de Montréal. L'objectif du projet consiste à produire une démonstration de faisabilité comprenant les outils d'exploration suivants :

- un point d'accès SPARQL;
- des URI déréférençables menant à des fiches d'informations;
- différentes sérialisations du jeu de données;
- une documentation.

L’échantillon de données produit dans le cadre de cette démonstration est principalement lié au secteur du Faubourg à m’lasse, dont une large superficie fut détruite en 1963 pour faire place à la construction de la maison de Radio-Canada. Dans une moindre mesure, certaines informations concernant d’autres éléments de patrimoine disparu seront rendues disponibles afin d’esquisser le contexte plus large d’un quartier disparu à Montréal.

## Version courante du graphe

La dernière version du graphe basé sur le modèle en cours de développement est disponible par le point d’accès SPARQL suivant :

- [http://qdmtl.ca/sparql](http://qdmtl.ca/sparql)

> :warning: **NOTE** :warning:
>
> Il s'agit d'une prépublication : la structure et le contenu du jeu de données pourraient être substantiellement modifiés dans les prochaines semaines.


## Méthodologie de développement

Approche méthodologique principale : *Simple Agile Methodology for Ontology Development* (SAMOD), méthodologie décrite par Peroni : https://essepuntato.it/samod/.

## Branches de ce dépôt

- `main` : dernière version de l’ontologie (TBox)
- `dev` : version de développement
- `tc-<ID>` : les branches identifiées par la forme `tc-<ID>`, où `<ID>` représente un numéro d’identification, sont associées aux cas de test effectués dans le cadre du développement de l’ontologie. Une ABox propre au cas de test est associée à la TBox afin de mener les *data tests* et les *query tests*.

<!--

## Documentation et cas de test

Les cas de test effectués dans le cadre du développement de cette ontologie constituent la seule documentation disponible à ce jour. Une documentation structurée sera publiée prochainement.

Les documents et les données liés aux cas de test sont disponibles dans ce dépôt :

- lien.

-->

## Ressources

- Informations sur le projet `QDMTL` : [https://qdmtl.ca](https://qdmtl.ca)
- Documentation : [https://qdmtl.ca/doc](https://qdmtl.ca/doc)
- Visualisation du modèle : [https://qdmtl.ca/modele](https://qdmtl.ca/modele)
- SPARQL Endpoint : [http://data.qdmtl.ca/sparql]