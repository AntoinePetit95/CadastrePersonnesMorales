# Énergie Foncière – Parcellaire PM
*Le foncier des personnes morales, simplement !*

Énergie Foncière met gratuitement à disposition Parcellaire PM, une application Streamlit pour explorer 
les fichiers officiels des parcelles détenues par des personnes morales. L’objectif est simple : 
rendre une donnée publique, utile mais difficile à manipuler, enfin exploitable en quelques clics, 
sans devoir ouvrir et croiser de lourds fichiers CSV.

Nous avons conçu cet outil pour simplifier le travail de nos clients et, plus largement, de tous les 
acteurs du foncier : développeurs ENR, bureaux d’études, collectivités, notaires, géomètres, aménageurs, 
agriculteurs, etc.

## Accéder à l’application
Application Streamlit : https://energie-fonciere-parcellaire-pm.streamlit.app/

## À quoi sert l’outil ?
Les fichiers PPM (Parcelles des Personnes Morales) sont fournis par l’État et mis à jour chaque année. 
Ils contiennent des informations très riches, mais la structure est “brute” (niveaux fins comme 
les SUF, multiples lignes par parcelle et/ou par propriétaire, volumes importants, etc.).

Parcellaire PM permet de :
- retrouver rapidement les personnes morales associées à une parcelle (ou une liste de parcelles) ;
- rechercher les parcelles associées à une personne morale via un numéro SIREN ;
- effectuer une recherche textuelle par nom (avec options de recherche complète / incomplète) ;
- télécharger le résultat dans un fichier lisible, en choisissant un niveau de détail adapté à votre besoin.

## Comment l’utiliser (workflow recommandé)
L’application fonctionne en 4 étapes :
1. Choisir un mode de recherche.
2. Choisir une ou plusieurs références (parcelles, numéro SIREN, dénomination).
3. Lancer la requête sur la ou les références.
4. Choisir les options de format, puis télécharger le fichier.

### 1) Recherche par parcelles
- Saisissez une ou plusieurs références cadastrales (parcelles).
- Ajoutez-les à votre liste.
- Lancez la recherche.

Cas d’usage typique : identifier rapidement quels organismes (sociétés, établissements publics, etc.) 
possèdent des droits sur une ou plusieurs parcelles ciblées.

### 2) Recherche par numéro SIREN
- Saisissez un ou plusieurs numéros SIREN.
- Limitez la recherche à un ou plusieurs départements.

Pourquoi limiter aux départements ?
Sans limitation, la recherche nécessite de parcourir l'intégralité la base, ce qui est long. 
Restreindre à des départements ciblés améliore fortement les temps de réponse.

*Attention : certaines entrées de la base comportent un numéro SIREN ne correspondant pas à la réalité, 
mais à une référence interne utilisée par les services de l'état.*

Cas d’usage typique : obtenir les parcelles associées à une entité précise 
(ex : un établissement public, une grande foncière, une société de projet, etc.), 
sur un périmètre géographique choisi.

### 3) Recherche par nom
- Saisissez du texte (nom partiel ou complet).
- Choisissez le mode de recherche (complète / incomplète).
- Limitez, là aussi, à un ou plusieurs départements pour garder une recherche rapide et pertinente.

Cas d’usage typique : retrouver une entité dont on n’a pas immédiatement le SIREN, 
ou vérifier si une entité personne morale n'apparait pas ailleurs dans la base sans que le numéro SIREN 
ne corresponde.

## Options de format avant téléchargement
Une fois les résultats affichés, vous pouvez choisir le format le plus adapté :

**Grouper les SUF** : Les SUF (subdivisions fiscales) sont des sous-unités de parcelles. Elles sont souvent 
peu pertinentes pour une lecture “foncière” standard.
- activé : les champs SUF sont concaténés (ex : "A|B")
- désactivé : une ligne par SUF (plus détaillé)  

**Grouper les PM** : Permet de regrouper (ou non) les personnes morales sur une même parcelle.
- activé : les champs personnes morales sont concaténés (ex : "ETAT|ONF")
- désactivé : une ligne par personne morale (plus détaillé)  

**Simplifier** : Permet de retirer certaines informations secondaires présentes dans la source 
pour obtenir un fichier plus lisible et directement exploitable.

Vous pouvez ensuite télécharger le fichier :
- soit en version “simplifiée” (lisible, orientée usage),
- soit en version “entière” (détaillée, proche de la source).

## Données et périmètre
L’outil s’appuie sur les fichiers “locaux et parcelles des personnes morales” publiés sous Licence Ouverte / Open Licence 2.0.
Parcellaire PM exploite uniquement la partie “propriétés non bâties (parcelles)”.

Source officielle : https://www.data.gouv.fr/fr/datasets/fichiers-des-locaux-et-des-parcelles-des-personnes-morales/

## Bonnes pratiques (performance)
- Pour les recherches par SIREN et par nom, limitez la recherche à un ou plusieurs départements.
- Préférez une liste de références cohérente (même zone géographique) pour obtenir des résultats rapides.
- Utilisez les options de regroupement (SUF / PM) pour adapter le niveau de détail à votre besoin.

## À propos d’Énergie Foncière
Énergie Foncière accompagne les porteurs de projets et les acteurs du territoire sur 
les sujets fonciers : qualification, prospection, négociation, sécurisation, formation et audit. 
Parcellaire PM illustre notre conviction : une donnée foncière bien structurée et 
bien présentée fait gagner du temps, réduit les erreurs et améliore la qualité des décisions.

Retrouvez-nous sur notre site internet : https://energie-fonciere.fr/

## Contact / retours
Vous avez une suggestion, un bug à signaler, ou un besoin d’évolution ?
Contactez-nous via [LinkedIn](https://www.linkedin.com/in/antoine-petit-ef/), 
ou ouvrez un ticket sur le [dépôt GitHub](https://github.com/AntoinePetit95/EF_PPM/tree/master) du projet.


## Avertissement
Cet outil vise à faciliter la lecture et l’exploitation de données publiques. Il ne remplace pas une analyse juridique complète (titres, servitudes, baux, indivisions, etc.) ni une vérification auprès des sources officielles et des professionnels compétents.
