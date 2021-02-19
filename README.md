<<<<<<< HEAD
# ChatonCTF, votre assistant félin pour les CTF

## Installation

Commencer par installer les dépendances nécessaires pour l'utilisation.

```python
pip install -r requirements.txt
```

Puis importer dans votre script chatonCTF
=======
# ChatonCTF, votre assitant félin pour les CTF

## Installation

Installer les dépendences utiliser par le module:

```bash
pip install -r requirements.txt
```

puis dans votre script importer le module
>>>>>>> 1eda113 (	nouveau fichier : README.md)

```python
import chatonCTF
```

<<<<<<< HEAD
## Explications

ChatonCTF est un module python à charger pour faciliter les challenges.

pour le moment, il est capable des options suivantes:

### FlagFinder

En lui passant un pattern et un fichier, le chaton est capable de chercher sa cible et de stocker le résultat dans un fichier flag.txt

### Binary Scan/Extract

Avec cette option, le chaton peut scanner et/ou extraire les données d'un firmware.

### RSA

Le chaton peut vous aider avec les challenges RSA en calculant les données suivantes:

- Calculer **N** si vous avez **P** et **Q**
- Calculer **P** ou **Q** si vous avez **N** et un membre du binôme à trouver
- Calculer **Phi(n)** si vous lui fournissez **P** et **Q**
- Calculer **D** Si vous avez **Phi(n)** et **E**

## Outro

ChatonCTF est modulaire, et sera mis à jour au fur et à mesure que j'apprendrai de nouvelles techniques
=======
## Fonctionnalités

### ReverseString

inverser une chaine de caractères (ex: 1234 <---> 4321)

### FlagFinder

trouver un flag dans un fichier en lui fournissant un regex

### BinScan/BinExtract

en s'aidant de binwalk, il est capable de scanner/extraire un firmware

### RSA

fonctions possibles:

- Calculer **N** à partir de **P** et de **Q**
- Calculer **P** ou **Q** à partir de **N** et d'un des membres du binôme
- Calculer **Phi(n)** à partir de **P** et de **Q**
- Calculer **D** à partir de **Phi(n)** et de **E**
>>>>>>> 1eda113 (	nouveau fichier : README.md)
