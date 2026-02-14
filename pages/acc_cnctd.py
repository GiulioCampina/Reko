import streamlit as st
import dtbs_fct as dbts
import folium
import streamlit_folium as sf
import folium.plugins as fp
import fl_fct as fctfl

st.set_page_config(initial_sidebar_state="collapsed", layout="wide")

st.title("Bienvenue parmi nous "+ f":red[{st.session_state.get('usnm')}]")

col_frd, col_map = st.columns([3, 8])

with col_frd:
    with st.container(border=True):
        st.header("Ajoute tes amis ici !")
        rch = st.text_input("Écris le nom de ton ami, puis :red[clique sur la touche entrée]")
        if dbts.user_exist(rch) is True:
            if dbts.deja_amis(st.session_state.get("usnm"), rch) is False:
                st.text("tu peux ajouter " + rch)
                if st.button(f"ajoute {rch}"):
                    if dbts.deja_amis(st.session_state.get("usnm"), rch) is True:
                        st.markdown("deja amis avec " + rch)
                    else:
                        dbts.add_friend(st.session_state.get("usnm"), rch, True)
            else:
                st.markdown("Vous etes déjà amis avec cet utilisateur!")
        else:
            st.markdown("Aucun utilisateur sous le nom de "+rch)

    with st.container(border=True):
        st.header("Liste de tes amis:")
        lst_amis = dbts.supabase.table("user_database").select('lst_frd').eq('username', st.session_state.get("usnm")).execute()
        afich_ams = ""
        for i in lst_amis:
            for j in i:
                if isinstance(j, list):
                    for k in j:
                        afich_ams = afich_ams +  k['lst_frd']
        st.markdown(afich_ams)
    with st.container(border=True):
        st.header("Nouvelle Reko")
        st.markdown(""""Pour cela, rien de plus simple : placez votre curseur à l’endroit où vous voulez ajouter une reko, puis récupérez les coordonnées en bas à droite pour localiser votre reko.
        """"")
        co_x = st.text_input("première coordonée en bas a droite ")
        co_y = st.text_input("deuxieme coordonnée")
        trt = st.text_input("Titre de la reko")
        dscp = st.text_input("Déscription du lieu. Alors : Reko ou pas reko ?!")
        if st.button("ajouter la reko"):
            dbts.ajt_reko(st.session_state.get("usnm"),trt, co_x, co_y, dscp)
            st.markdown("reko ajoutée a votre liste")
with col_map:
    with st.container(border=True):
        col_crt, col_fl = st.columns([7, 2])
        with col_crt:
            m = folium.Map(location=[48.692054, 6.184417], zoom_start=16, tiles="OpenStreetMap")
            fp.Geocoder().add_to(m)
            fp.MousePosition().add_to(m)
            reks = folium.FeatureGroup(name="reks")

            for rk in dbts.get_lst_reko_ami(st.session_state.get("usnm")):
                rk = rk.replace(' ', '')   # absolument essentiel, sinon ne reconnais pas le nom de la table ,
                # c'est plus proche de la magie qu'autre chose mais bon amen hein
                rk = rk.lower()
                lst_ajt = []
                #st.markdown(rk)
                #st.markdown(fctfl.gener_mrk(rk))
                for rek_amis_rk in fctfl.gener_mrk(rk):
                    lst_ajt.append(rek_amis_rk)
                #st.markdown(lst_ajt)
                for last_mrk in lst_ajt:
                    reks.add_child(
                        folium.Marker(
                            location=last_mrk[1],
                            tooltip=last_mrk[0],
                            popup=last_mrk[2]
    
    
                        )
                    )



            sf.st_folium(m, width=725, returned_objects=[], feature_group_to_add=reks)

        with col_fl:

            st.title("Reko recentes :")









