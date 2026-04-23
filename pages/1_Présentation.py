import streamlit as st
import pandas as pd
import components.components as comp

st.set_page_config(
    page_title="Do_it - Présentation",
    layout="wide"
)

st.title("Présentation de la filière 3A de Do_it")
st.markdown(
    """
<span style="color: red">D</span><span style="color: lightblue">o</span>_<span style="color: purple">It</span> est une option de troisième année au sein de l’école centrale Méditerranée. Elle s’appuie sur deux disciplines : l’Informatique et le Management des Systèmes d'information, pour enseigner le développement logiciel et la gestion.
Une grande liberté est donnée aux étudiants pour choisir leur formation au sein de cette option dont le cœur est une approche systémique des transformations socio-techniques liées à l’IT.

Do_It s’adresse ainsi à des élèves voulant :
- soit s’orienter vers le <span style="color: red">développement logiciel</span>,
- soit s’orienter vers le <span style="color: lightblue">management des systèmes d’information</span>,
- voulant <span style="color: purple">mélanger les connaissances</span> en management et en développement.

La spécificité de <span style="color: red">D</span><span style="color: lightblue">o</span>_<span style="color: purple">It</span> – outre le mix inédit de deux disciplines permettant de comprendre les intrications entre la technique et l’humain – est que chaque élève est suivi par un tuteur (les responsables de chaque axe) qui l’aide à créer un plan d’apprentissage pour chaque temps (différent selon le bagage de chaque élève). Ce plan sera composé à partir des cours en présentiel et des connaissances disponibles en auto-formation pour que l’élève puisse mener à bien ses projets et préparer son entrée dans la vie active.

Un élève pourra, selon son projet professionnel, mixer les spécialisations disciplinaires ou rester mono couleur. Il pourra, à chaque temps, substituer un MON (Monitoring of Novelties) à un CS (cf plus loin le paragraphe MON). 

Enfin, Do_It est en partenariat avec les masters  GIG (géométrie et informatique graphique) et IMD (informatique et mathématiques discrètes), que les élèves — s’ils le souhaitent et sous réserve d’acceptation par les responsables des différents masters — peuvent suivre en parallèle (les horaires sont aménagés).
""", unsafe_allow_html=True
)
st.subheader("Emploi du temps")
df = pd.DataFrame({
    '':['Temps 1', 'Temps 2', 'Temps 3'],
    'Tronc Commun':['18h','',''],
    'Cours de Spécialité':['4x18h','4x18h','4x18h'],
    'POK1':['10h','14h',''],
    'POK2':['','14h','10h'],
    'Projet 3A':['27h','27h','45h']
})
st.dataframe(df,hide_index=True)
comp.footer()