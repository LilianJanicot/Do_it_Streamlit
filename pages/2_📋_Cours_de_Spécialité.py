import streamlit as st
import components.components as comp
st.set_page_config(
    page_title="Cours",
    layout="wide",
    page_icon=comp.path_logo()
)
st.title("Cours de spécialité en 3A")

option = st.selectbox(
    'Sélectionner un temps pour voir les CS disponibles',
    ["Temps 1", "Temps 2", "Temps 3"])

left_column, right_column = st.columns(2, vertical_alignment="top")

with left_column:
    st.html(
        '<h2 style="color: red;">Informatique</h2>'
        )
with right_column:
    st.html(
        '<h2 style="color: lightblue;">Organisation</h2>'
        )

with left_column:
    if option == "Temps 1" :
        comp.course_card("Méthode de développement",
                         "Ce cours permet d'acquérir des compétences en méthode de développement. Le cours se basera sur le langage Python mais peut-être appliqué à n'importe quel langage de programmation. Nous verrons comment déboguer un code, programmer en objet sous Python, créer un environnement virtuel, utiliser git et GitHub et finalement, programmer par les tests.",
                         "François Brucker")
        comp.course_card("System design",
                         "Un cours pour apprendre à concevoir des systèmes logiciels solides, scalables et bien pensés. Tech en priorité, avec une dose de produit pour choisir les bonnes fonctionnalités, et de data pour mesurer leur impact. Un bon point d’entrée vers les réalités du développement en entreprise.",
                         "Adèle Bourgeix")
        comp.course_card("Développement Web: from 0 to hero",
                         "Décortiquons ensemble une architecture simple d’un site « moderne » avec un backend et un frontend séparés qui communiquent ensemble. A l’issue du cours, vous serez en capacité de gérer le développement d’une API et de l’exploiter sur une interface. Une approche par le test sera privilégiée tout au long du développement.",
                         "Adrien Brunet & Nicolas Bert")
    elif option == "Temps 2" :
        comp.course_card("Linux",
                         "Initiation au monde unix et à l’utilisation du terminal. On montrera comment est organisé et configuré un système d'exploitation Unix et de comment installer un système Linux. Ces connaissances vont permettre de gérer les serveurs distant pour exécuter les services web. On utilisera pour cela un serveur de test qui sera accessible tout au long de l’année et qui pourra accueillir les déploiements des différentes applications web créées au cours de l'année.",
                         "François Brucker & Geoffroy Desvernay")
        comp.course_card("Java / gradle",
                         "Le cours se divise en deux parties : Approfondir les notions de conception orientée objet en Java (design patterns) puis découverte du framework Spring Boot et de l'outil de build Gradle (réalisation d'un projet WEB / API REST).", "programmation orientée objet (Python) / SGBD et SQL / un peu de HTML et CSS (web) / Git.",
                         "Julien Candela",)
        comp.course_card("Structures de Données",
                         "Le design d’une structure de donnée au problème que l’on cherche à résoudre est indispensable pour obtenir des algorithmes efficaces. On verra dans ce cours des structures classiques (arbres de recherches équilibrés, tas, tas binomiaux, table de hachage) ainsi que les éléments fondamentaux (points, pile et file) pour concevoir et implémenter de telles structures. Enfin, on y montrera également des notions d’analyse amorite pour le calcul de la complexité de l’usage de ces structures.",
                         "Pascal Préa")
    else:
        comp.course_card("Aws/docker",
                         "Utilisation de [Docker](https://www.docker.com/) et de [Aws Cloud](https://aws.amazon.com/fr/) d’Amazon",
                         "Thomas Brien",
                         "avoir développé un application web / Github et Github actions / compte AWS gratuit")
        comp.course_card("Réseau",
                         "**Cours accessibles et utiles à tout élève voulant utiliser des outils informatiques sans en faire un métier** \n\n Comment comprendre et configurer un réseau local comme vous pouvez en avoir un chez vous.",
                         "Patrick Girard")
        comp.course_card("Cryptographie",
                         "On utilisera le prétexte de la sécurité informatique pour montrer et démontrer divers algorithmes de cryptographie ainsi que les moyens de les utiliser via des protocoles de transmission de données.\n\nCe cours est résolument tourné vers la théorie et l’algorithmie (avancée) : nous n’y traiterons ni de sécurité informatique ni de développement logiciel. Le matériel nécessaire pour suivre cette UE sera du papier, un crayon et une gomme couplée à une envie débordante de faire des mathématiques discrètes.",
                         "François Brucker")

with right_column:
    if option == "Temps 1" :
        comp.course_card("Organisation & IT","Qu’est-ce qu’un système d’information ? Quels sont les liens entre les processus de gestion des organisations et les systèmes d’information ? Quelles sont les évolutions des fonctions et des configurations des SI en lien avec la transformation des entreprises et des organisations ? Ce cours pose les bases fondamentales de l’analyse organisationnelle en lien avec le management des SI et la transformation numérique des organisations. Il introduit les notions d’architecture et d’urbanisation des SI.")
        comp.course_card("Travail & numérique","Ce cours explore, via sociologie et psychologie du travail, l’impact du numérique et de l’IA sur les organisations. Il analyse les plateformes numériques comme outils techniques et sociaux, et souligne l’importance d’intégrer l’expérience utilisateur et les besoins réels des salariés dans la conception des solutions digitales. En s’appuyant sur les neurosciences et des méthodes comme l’entretien d’explicitation, il vise à améliorer la réussite des projets de transformation, souvent en échec faute d’approche humaine adaptée.")
        comp.course_card("Numérique responsable / Responsabilité numérique des organisations","Ce cours aborde la responsabilité numérique des organisations, à la croisée du développement durable et de la transformation digitale. Il explore les enjeux éthiques, juridiques et environnementaux des écosystèmes IT, en mettant l’accent sur la sobriété, l’accessibilité et la souveraineté numérique. L’objectif : outiller les organisations pour une transition numérique durable, en analysant l’impact socio-économique et le cycle de vie des technologies.")
    elif option == "Temps 2" :
        comp.course_card("Stratégie & gouvernance des SI","Ce cours permet de positionner les systèmes d’information comme une pièce maîtresse de la stratégie d’entreprise.\n- les SI et les innovations IT comme éléments différenciant pour les organisations dans un contexte concurrentiel\n- l’alignement stratégique des SI pour s’assurer de leur cohérence et contribution à la stratégie globale des entreprises\n- les alternatives entre externalisation et internalisation des SI (cloud)\n- les outils et méthodes de pilotage de la fonction SI en lien avec la stratégie (Schéma directeur des systèmes d’information.")
        comp.course_card("Conception des SI et business process management","Ce cours enseigne la conception des systèmes d’information, en alignant SI et processus métiers. Sur 6 demi-journées, il couvre : lien SI-business (CRM), business case, audit organisationnel et choix d’outils. Alternant théorie et pratique, il forme à l’outil Bizagi Modeller, avec l’appui de consultants. L’objectif : structurer le SI selon les besoins réels de l’entreprise, sans prérequis en stratégie IT.")
        comp.course_card("UX Design / ergonomie des systèmes d’information","Le module introduit les démarches en ergonomie et en Design d’Expérience Utilisateur (UX Design), en les intégrant à la conception de solutions numériques. Il souligne l’importance des facteurs humains et de la psychologie cognitive pour créer des interfaces inclusives et centrées sur les utilisateurs finaux, tout en tenant compte des enjeux stratégiques et des contraintes du projet. Les étudiants apprendront et appliqueront diverses méthodologies tout au long du processus, notamment la conception d’interfaces numériques avec l’outil Figma.")
    else:
        comp.course_card("IT & transformations organisationnelles : des enjeux à la mise en oeuvre","Ce cours présente les problématiques managériales associées au changement et les méthodologies pour l’accompagner, en s’appuyant sur le cas pratique du déploiement des solutions d’IA agentique. Il introduit aussi des perspectives critiques pour décrypter les “résistances au changement” et proposer des outils analytiques issus de la sociologie afin de mieux les comprendre et peut-être les surmonter.")
        comp.course_card("Cybersécurité et management des risques","Quelles sont les vulnérabilités auxquelles l’IT expose les organisations ? Comment peuvent-elles s’en prémunir tant sur le plan technique qu’humain et organisationnel ?  Ce module introduit des notions essentielles sur la réglementation relative aux données personnelles. Il présente les enjeux organisationnels de la cybersécurité, avec des témoignages professionnels et une simulation de crise cyber. Il donne un panorama d’ensemble sur les fonctions et outils du SOC (security operation center).")
        comp.course_card("Monitoring des SI (économie et pilotage de l’IT)","Quels sont les indicateurs de performance et de “bonne santé” des serveurs, des applications, des containers … ? Comment optimiser sur les plans technique et économique l’usage des infrastructures IT ? Au carrefour des enjeux financiers et du maintien en conditions opérationnelles des systèmes, ce module vous amènera à mettre en pratique les enjeux d’observabilité des SI.")

comp.footer()