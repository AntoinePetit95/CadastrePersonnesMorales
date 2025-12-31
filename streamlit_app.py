import os
import streamlit as st


logo_path = f".{os.sep}EF_PPM{os.sep}assets{os.sep}LOGO-EF-RVB.svg"
icon_path = f".{os.sep}EF_PPM{os.sep}assets{os.sep}LOGO_CARRE.png"

help_outil = ("**Parcellaire PM** est un outil gratuit conçu par **Énergie Foncière** pour simplifier "
              "l’exploitation des fichiers annuels de parcelles détenues par des personnes morales. "
              "À partir d’une parcelle ou d’une liste de références cadastrales, il permet d’identifier "
              "les propriétaires concernés puis d’exporter les résultats.")

st.set_page_config(
    page_title='Parcellaire PM',
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
    st.title("Parcellaire PM", help=help_outil)
    st.caption("*Le foncier des personnes morales, simplement !*")
    bas_de_page = st.container(vertical_alignment='bottom')
    bas_de_page.caption("Données : septembre 2025")

pages = {
    "Recherche": [
        st.Page("page_par_parcelle.py", title="Par parcelle", icon="1️⃣"),
        st.Page("page_par_siren.py", title="Par SIREN", icon="🪪"),
        st.Page("page_par_nom.py", title="Par dénomination", icon="💬")
    ],
    "Ressources": [
        st.Page("page_readme.py", title="Lisez-moi", icon="📰"),
    ]
}

pg = st.navigation(pages, expanded=True, position='sidebar')

pg.run()

