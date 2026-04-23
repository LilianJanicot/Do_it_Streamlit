# Do_it_Streamlit
Projet pour transformer la présentation de l'option 3A Do-it en un site internet hébergé localement via le module streamlit. C'est plus beau et plus lisible qu'un google document :)

Le projet utilise le module streamlit de python car il est facile à utiliser et prendra peu de temps de code pour un résultat plus que convenable.
Le module streamlit lance un serveur en local pour héberger un site internet.

# Comment lancer le projet?
### Initialisation
La première fois que vous lancez le projet, il faut installer les modules obligatoires. A l'aide du terminal de commande, allez dans le dossier du projet et lancez la commande :
```
pip install -r requierements.txt 
```
Le module est un peu lourd (plusieurs Mo) et dépend de beaucoup d'autres modules. Attendez vous à attendre une petit minute pour l'installation. C'est le temps parfait pour aller vous faire un thé ou un chocolat chaud :)
 
### Lancer le site internet
Dans le dossier du projet, lancez la commande :
```
streamlit run Accueil.py
```
pour lancer le serveur ainsi que le site internet.

# Comment le fichier requirements.txt est généré?
Dans le dossier du projet, lancez :
```
pip freeze > requirements.txt
```