import streamlit as st
from streamlit_extras.bottom_container import *

def footer():
    with bottom() :
        st.markdown("---")
        st.markdown(
        """
        <font size="2">*Ce site n'a fait l'objet d'aucune validation officielle de la part de l'école. Il est destiné à être un outil de communication et de partage d'informations pour les étudiants.
        Les informations sur le site peuvent donc être incomplètes ou obsolètes, et il est recommandé de vérifier les informations auprès des sources officielles de l'école pour toute question ou préoccupation.*</font>
        """, unsafe_allow_html=True
        )
        st.write("© 2026 Lilian Janicot. Tous droits réservés. Le site n'a pas été généré par une IA. Version 0.1")

def course_card(course_name, course_desc, course_teachers):
    st.subheader(course_name)
    st.markdown(f"**Enseignant(s)** : {course_teachers}")
    st.write(course_desc)