import streamlit as st
from pathlib import Path
import components.components as comp

BASE_DIR = Path(__file__).resolve().parent.parent  # remonte à "projet"
image_path1 = BASE_DIR / "components" / "images" / "tortuegenial.png"
image_path2 = BASE_DIR / "components" / "images" / "goupix.png"


st.set_page_config(
    page_title="Responsables",
    layout="wide",
    page_icon=comp.path_logo()
)

st.title("Responsables de la filière Do_it")
st.markdown(
    """
    La filière Do_it est encadrée par deux responsables pédagogiques. Vous trouverez leurs coordonnées ci-dessous. N'hésitez pas à les contacter pour toute question ou demande d'information sur la filière !
"""
)

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Responsable informatique")
    st.image(image_path1)
    st.markdown(
        """
        **François Brucker**  
        Email : francois.brucker@centrale-med.fr
        """
    )
with right_column:
    st.subheader("Responsable management")
    st.image(image_path2)
    st.markdown(
        """
        **Laetitia Piet**  
        Email : laetitia.piet@centrale-med.fr
        """
    )

comp.footer()