import streamlit as st
import dtbs_fct as dbfc

st.set_page_config(initial_sidebar_state="collapsed")
st.title("Connecte toi à ton compte!")


usnm = st.text_input("Pseudonyme")
motdp = st.text_input("Mot de passe ")

if usnm is None:
    usnm = "grosrelou"

if st.button("Connexion"):
    if motdp == dbfc.get_mdp(usnm):
        st.session_state["usnm"] = usnm
        st.session_state["motdp"] = motdp
        st.switch_page("pages/acc_cnctd.py")
    elif dbfc.get_mdp(usnm) is None:
        st.markdown("Erreur de pseudonyme")
    else:
        st.markdown("Erreur de mot de passe")


