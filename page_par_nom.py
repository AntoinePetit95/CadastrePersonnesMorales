import streamlit as st

from CPM.retriever.retriever import PPM
from CPM.utils.dept_code import DEPARTEMENTS_CODES, DEPARTEMENTS


@st.fragment
def affiche_tableau(ppm:PPM) -> None:

    ppm_to_show = ppm

    help_suf = ("La **subdivision fiscale (suf)** est une partie de parcelle ayant la même nature de culture "
                "(c’est-à-dire la même affectation fiscale). Il est très rare que les SUF d'une même parcelle "
                "aient des propriétaires différents, il est conseillé de les regrouper pour une lecture plus simple.")
    group_by_suf = st.toggle("Regrouper les SUF (recommandé)", help=help_suf, value=True)
    if group_by_suf:
        ppm_to_show = ppm_to_show.merged_suf

    help_pm = "Grouper les propriétaires sur une seule ligne."
    group_by_pm = st.toggle("Regrouper les propriétaires", help=help_pm, value=False)
    if group_by_pm:
        ppm_to_show = ppm_to_show.merged_rights

    help_essential = "Ne conserver que les informations essentielles."
    show_only_essential = st.toggle("Simplifier (recommandé)", help=help_essential, value=True)
    if show_only_essential:
        ppm_to_show = ppm_to_show.essential

    ppm_to_show.sort_by_idu()

    styler = ppm_to_show.na_as_empty_string().table.style.hide().bar(
        subset=['contenance'], align="mid", color="#82C46C"
    ).set_table_styles([
          {"selector": "th", "props": [("font-size", "11px")]},           # en-têtes
          {"selector": "td", "props": [("font-size", "11px")]},           # cellules
      ])

    with st.container(height=300):
        st.write(styler.to_html(), unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    c2.caption(f"{len(ppm_to_show.table)} lignes", text_alignment='right')
    downloaded = c1.download_button(
        "Télécharger la table",
        data=ppm_to_show.excel_file_bytes,
        mime="application/octet-stream",
        file_name="Énergie_Foncière_parcellaire_PM.xlsx",
    )

    if downloaded:
        st.success("**Et voilà !**   \n   \n[**Énergie Foncière**](https://energie-fonciere.fr/) "
                   "met cet outil à disposition pour simplifier l’accès à "
                   "la donnée foncière.   \nCela vous a été utile ? Laissez-nous un "
                   "👍 [**avis Google**](https://g.page/r/CXS-zJLN66DrEAE/review) ou "
                   "💬 [**discutons ensemble**](https://www.linkedin.com/in/antoine-petit-ef/) !")


def initialize_values() -> None:
    values = {
        'nom': None,
        'mode': 'contains',
        'departements': [],
        'ppm_nom': PPM(),
    }
    for k, v in values.items():
        if k not in st.session_state.keys():
            st.session_state[k] = v

initialize_values()

st.subheader("💬 Recherche par dénomination")

def format_function(dept_code: str) -> str:
    return f"{dept_code} - {DEPARTEMENTS[dept_code]}"

st.multiselect(
    "Départements de recherche",
    DEPARTEMENTS_CODES,
    format_func=format_function,
    key='departements',
    placeholder='Limiter la recherche aux départements ...'
)
if len(st.session_state['departements']) >= 3:
    st.warning(f"Beaucoup de départements ont été sélectionnés, cela peut ralentir la recherche.")


def interroge_base() -> None:
    if not st.session_state['nom']:
        return
    if not st.session_state['departements']:
        return

    with st.spinner("Récupération des informations ...", show_time=True):
        ppm = PPM()
        ppm.fetch_name(
            name=st.session_state['nom'].upper(),
            limit_to_department=st.session_state['departements'],
            mode=st.session_state['mode']
        )
        st.session_state['ppm_nom'] = ppm

    if ppm.empty:
        st.info('Aucun résultat !', icon='🫥')
    else:
        st.success("Informations récupérées !", icon="🎉")
        affiche_tableau(st.session_state['ppm_nom'])

def resultats(_id: str) -> None:
    st.divider()
    nom_est_correct = True

    if st.session_state['nom'] is None:
        nom_est_correct = False
    elif st.session_state['nom'] == '':
        nom_est_correct = False
    elif not len(st.session_state['nom']) >= 2:
        st.warning('Entrez au moins 2 caractères')
        nom_est_correct = False

    disabled = not nom_est_correct

    if not nom_est_correct:
        disabled = True

    if not st.session_state['departements']:
        disabled = True

    cr1, cr2 = st.columns([5,2], vertical_alignment="center")

    bouton_interroger = cr2.button(
        icon='🔍',
        label=f"interroger la base",
        disabled=disabled,
        type='primary',
        key=f"query_button_{_id}",
        width='stretch'
    )
    if bouton_interroger:
        interroge_base()

with st.container(border=True):
    st.text_input("Dénomination de la personne morale", placeholder="SCI des Tilleuls", key='nom')

    options = {
        "contains": "Contient",
        "exact": "Correspondance exact",
    }
    format_function = lambda x: options[x]

    st.pills("Mode", options=options.keys(), format_func=format_function, key='mode')

    resultats("Dénomination")

