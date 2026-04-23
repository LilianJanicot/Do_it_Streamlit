import streamlit as st
import components.components as comp

st.set_page_config(
    page_title="Do_it - POK&MON",
)

st.title("Présentation des projets POK et MON")
st.subheader("Les MON")
st.markdown(
    """
Je me POK le MON
"""
)
st.subheader("Les POK")
st.markdown(
    """
Je me MON le POK
"""
)
comp.footer()