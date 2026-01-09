# Python Personnal Learning
Bienvenue dans ce repo qui va me permettre de centraliser les différentes notions python intermédiaires (notions théorique et applications)

## 1) PEP8 :
Il s'agit d'un ensemble de règles de style recommandées pour la programmation en python. Ces règles permettent d'écrire du code propre, facile à relire, à corriger et à maintenir.

Ces règles comprennent des notions importantes  comme :
- Pour qu'un code soit réutilisable, il faut qu'une fonction == une feature et pas plus ;
- La nommenclature des variables permet une lecture plus simple par un autre développeur que le créateur ;
- Ne pas dépasser 79 caractères par ligne pour garder un code lisible ;
- Les fonctions doivent être nommées en fonction de leur utilité final ;
- Ajout de commentaires et docstring pour une meilleur compréhension du code ;


ref : https://schane-lune.forge.apps.education.fr/1nsi/05_langage-programmation/pep8/


## 2) Les Dataclasses :

Les **dataclasses** permettent de se concentrer sur la définition des attributs en laissant python gérer le reste.

Exemple :
```python
from dataclasses import dataclass

@dataclass
class Task:
    id: str
    status: str
```

ref :
- https://www.docstring.fr/glossaire/dataclasses/ --> Docstring.fr
- https://www.datacamp.com/fr/tutorial/python-data-classes --> Datacamp.com
- https://docs.python.org/3/library/dataclasses.html --> Documentation python