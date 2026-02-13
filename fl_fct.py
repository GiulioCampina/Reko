import streamlit as st
import folium
import streamlit_folium
import dtbs_fct as dbts
import supabase



def gener_mrk(target):
    target = target.strip()
    dta = dbts.supabase.table(target).select("*").execute().data
    nw_lst = []

    for row in dta:  # row est un dictionnaire
        trt = row['nom']
        location = [row['var_a'], row['var_b']]
        desc = row['nick_nm']

        nw_lst.append([trt, location, desc])

    print("Rendu final ////////")
    print(nw_lst)
    return nw_lst

