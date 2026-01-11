import os
import streamlit as st


logo_path = f".{os.sep}CPM{os.sep}assets{os.sep}LOGO-EF-RVB.svg"
icon_path = f".{os.sep}CPM{os.sep}assets{os.sep}LOGO_CARRE.png"

help_outil = ("Le **cadastre des personnes morales** est un outil gratuit conçu par **Énergie Foncière** "
              "pour simplifier l’exploitation de la donnée des parcelles détenues par des personnes morales. "
              "À partir d’une parcelle ou d’une liste de références cadastrales, identifiez "
              "les propriétaires concernés puis exportez les résultats.")

st.set_page_config(
    page_title='Cadastre des personnes morales',
    page_icon=icon_path,
    initial_sidebar_state='expanded',
)

with st.sidebar:

    st.logo(
        image=logo_path,
        icon_image=icon_path,
        size='large',
        link='https://energie-fonciere.fr/'
    )

    pages = {
        "Accueil": [st.Page("accueil.py", title="Accueil", icon="🏠")],
        "Recherche": [
            st.Page("page_par_parcelle.py", title="Par parcelle", icon="1️⃣"),
            st.Page("page_par_siren.py", title="Par SIREN", icon="🪪"),
            st.Page("page_par_nom.py", title="Par dénomination", icon="💬")
        ],
        "Ressources": [st.Page("page_readme.py", title="Lisez-moi", icon="📰")]
    }
    pg = st.navigation(pages, expanded=True, position='sidebar')

    st.caption("Données : septembre 2025")

st.header("Cadastre des personnes morales", help=help_outil)


pg.run()

