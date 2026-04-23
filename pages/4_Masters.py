import streamlit as st
from streamlit_extras.bottom_container import *

st.title("Masters proposés en parallèle de Do_it")

st.markdown(
    """
Il est possible de suivre un master 2 en parallèle de Do_It. Suivre un double cursus est engageant et demande du travail supplémentaire, mais le gain est substantiel car il permet de colorer votre profil avec des compétences valorisées par un diplôme universitaire. 

Les deux M2 possibles sont : 
- [GIG](https://sciences.univ-amu.fr/fr/formation/masters/master-informatique/parcours-geometrie-informatique-graphique-gig) (Géométrie et Informatique Graphique) pour approfondir ses compétences en programmation graphique 
- [IMD](https://formations.univ-amu.fr/fr/master/5SIN/PRSIN5AD) (Informatique et Mathématiques Discrètes) pour approfondir les aspects théoriques de l’informatique

Il n'y a actuellement aucun master 2 d'organisation proposé en parallèle de Do_it.

Les cours de M2 sont condensés sur 2 temps. L’intégration avec l’option est la suivante pour ces deux temps :
- un des 2 premiers temps est entièrement consacré aux enseignements du master (temps 2 pour GIG par exemple)
- vous devrez suivre en plus de vos CS quelques cours du M2 pendant l’autre temps

Enfin, **suivre un M2 vous engage à choisir un stage de 3A en adéquation avec celui-ci**  (c’est à dire validé par le responsable du M2 que vous suivez).
"""
)

with bottom() :
    st.markdown("---")
    st.markdown(
    """
    <font size="2">*Ce site n'a fait l'objet d'aucune validation officielle de la part de l'école. Il est destiné à être un outil de communication et de partage d'informations pour les étudiants.
    Les informations sur le site peuvent donc être incomplètes ou obsolètes, et il est recommandé de vérifier les informations auprès des sources officielles de l'école pour toute question ou préoccupation.*</font>
""", unsafe_allow_html=True
)
    st.write("© 2026 Lilian Janicot. Tous droits réservés. Le site n'a pas été généré par une IA. Version 0.1")