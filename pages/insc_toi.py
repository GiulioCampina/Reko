import streamlit as st
import dtbs_fct
st.set_page_config(initial_sidebar_state="collapsed")
st.title("Bienvenue a bord , ton aventure sur :red[reko] debute ici")
st.markdown("""


Met ton nom et ton mot de passe dans les deux zones textuelles ci dessous! 
"""
            )

inp_nom = st.text_input("Votre nom d'utilisateur")
inp_mdp = st.text_input("votre mot de passe")

if st.button("S'inscrire:"):
    dtbs_fct.inscription(inp_nom, inp_mdp)

if st.button("Retour a la page d'aceuille"):
    st.switch_page("page_one.py")

