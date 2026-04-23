import streamlit as st
import components.components as comp

st.set_page_config(
    page_title="Do_it - POK&MON",
)

st.title("Présentation des projets POK et MON")
st.subheader("Les MON")
st.markdown(
    """
À chaque temps, il est possible de choisir un CS spécial appelé MON (Monitoring of Novelties). Le MON est un travail individuel sur un sujet **proposé par l’élève et validé par votre tuteur**. 

Choisir un MON permet de préparer les prérequis d’un CS d’un temps suivant, d'approfondir un sujet ou encore d’acquérir des connaissances sur un nouveau thème. Il est validé et évalué par un document et une soutenance.

Voici une liste non-exhaustive de MON acceptés par les tuteurs lors de l'année de 2025/2026 :
"""
)
st.markdown(
    """
    
- <span style="color:red">Clean API avec GraphQL</span>
- <span style="color:red">Formation Docker</span>
- <span style="color:lightblue">Conduite du changement dans les transformations digitales des DSI</span>
- <span style="color:lightblue">Elaboration d’une grille d’analyse à partir de lectures en sociologie urbaine</span>
""", unsafe_allow_html=True
)

st.subheader("Les POK")
st.markdown(
    """
Le POK (Proof of Knowledge) est un projet court (24h) permettant de mettre en pratique un savoir acquis pendant la formation. Le choix du sujet est libre mais il doit être validé par un tuteur pédagogique. Il est le plus souvent individuel mais peut être mené en binôme.

Quelques exemples de POK par temps.
- Temps 1 :
    - <span style="color:lightblue">Configurations organisationnelles dans le secteur de l'IT</span>
    - <span style="color:lightblue">Typologie des plateformes numériques</span>
    - <span style="color:red">Mon site chez moi</span>
    - ...
- Temps 2 :
    - <span style="color:lightblue">Cartographier le système d'information d'une organisation</span>
    - <span style="color:lightblue">Réaliser le diagnostic de la maturité de la transformation digitale d'une organisation</span>
    - <span style="color:red">Déployer un site web sur un serveur distant</span>
    - ...
- Temps 3 :
    - <span style="color:lightblue">Enquête sur le management algorithmique : enjeux économiques, sociaux et juridiques</span>
    - <span style="color:lightblue">Programmation par les tests d'un projet informatique</span>
    - <span style="color:red">Serverless et docker</span>
    - ...
""", unsafe_allow_html=True
)
comp.footer()