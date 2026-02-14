import dtbs_fct
import streamlit as st
import os

st.set_page_config(initial_sidebar_state="collapsed")
adrs_file = os.path.abspath(__file__)

st.title("Bienvenue sur :red[reko] ")
st.markdown(":orange[connecte] toi a ton profil ou :rainbow[inscris] toi!", )

if st.button(":rainbow[inscris toi]", icon="📝"):
    st.switch_page("pages/insc_toi.py")

if st.button(":orange[connecte toi]", icon="🔥"):

    st.switch_page("pages/cnx_pge.py")
