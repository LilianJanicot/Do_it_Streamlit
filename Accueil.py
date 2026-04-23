import streamlit as st
from streamlit_extras.bottom_container import *
import components.components as comp

st.set_page_config(
    page_title="Do_it - Accueil",
    layout="wide"
)
st.title("Bienvenue sur le site pour présenter la filière 3A de Do_it !")
st.markdown(
    """
    Ce site a été créé pour présenter les différentes activités et projets de la filière 3A de Do_it de l'école d'ingénierie généraliste Centrale Méditerranée.
    Vous y trouverez des informations sur les cours, les projets, les événements et les opportunités de la filière. N'hésitez pas à explorer le site et à contacter les responsables de la filière pour en savoir plus !

    Les différentes pages disponibles sont :
    - **Présentation** : une page pour présenter la filière et ses objectifs.
    - **Cours Disponibles** : une page pour présenter les différents cours proposés dans la filière.
    - **POK&MON** : une page pour présenter les projets POK et les MON.
    - **Masters** : une page pour présenter les différents partenariats de masters proposés dans la filière.
    - **Responsables** : une page pour présenter les différents responsables de la filière.

    
    En vous souhaitant une bonne navigation sur le site et qu'ils répondent à vos attentes !
    La version actuelle présente la filière pour l'année **2026/2027**.
"""
)

comp.footer()