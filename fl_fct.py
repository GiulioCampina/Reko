import streamlit as st
import folium
import streamlit_folium
import dtbs_fct as dbts
import supabase


def gener_mrk(target):
    dta = dbts.supabase.table(target).select("*").execute()
    nb = dbts.supabase.table(target).select("nom", count="exact").limit(0).execute()
    for i in nb:
        for e in i:
            if isinstance(e, int):
                nb = e

    location = []
    trt = ""
    desc = ""
    nw_lst = []
    tempo_lst = []
    for i in dta:
        for j in i:
            if isinstance(j, list):
                for reka in range(nb-1):
                    for k in j:
                        trt = k['nom']
                        location.append(k['var_a'])
                        location.append(k['var_b'])
                        desc = k['nick_nm']
                        tempo_lst.append(trt)
                        tempo_lst.append(location)
                        tempo_lst.append(desc)
                        nw_lst.append(tempo_lst)
                        tempo_lst = []
                        trt = ""
                        location = []
                        desc = ""

    print("REndu final ////////")
    print(nw_lst)
    return nw_lst



