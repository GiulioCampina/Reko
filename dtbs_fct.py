import re
from supabase import create_client
from clefs_id import url, key
import streamlit as st

supabase = create_client(url, key)


def get_mdp(username):
    """fct de recherche de mdp d'un username dans la liste donnée en paramètre"""
    mdp_fct = "flop_1"
    liste = supabase.table("user_database").select("*").execute()
    try:
        for i in liste:
            if isinstance(i, tuple):
                for e in i:
                    if isinstance(e, list):
                        for j in e:
                            if isinstance(j, dict):
                                if j['username'] == username:
                                    if j['pswrd'] is None:
                                        return mdp_fct
                                    else:
                                        return j['pswrd']
    except:
        return mdp_fct


# print(get_mdp("giu"))


def inscription(nom_user, mdp_inscr):
    alrdused = 0
    data = supabase.table("user_database").select("*").execute()
    # co_email = input("email")
    for i in data:
        if isinstance(i, tuple):
            for e in i:
                if isinstance(e, list):
                    for j in e:
                        if isinstance(j, dict):
                            if j['username'] == nom_user:
                                alrdused += 1
    if alrdused >= 1:
        st.markdown("pseudonyme deja utilisé")
    else:
        add_to_table_user(nom_user, mdp_inscr)
        new_tbl(nom_user)
        st.markdown("bienvenue parmi nous !!!")
        #add_friend(nom_user, 'reko_inc', False)


def add_to_table_user(nom, mdp):
    print("ajout de l'utilisateur {}".format(nom))
    supabase.table("user_database").insert({'username': nom, 'pswrd': mdp}).execute()
    return None


def new_tbl(user):
    new_table = """CREATE TABLE IF NOT EXISTS public.ma_table (
    nom TEXT NOT NULL,
    var_a FLOAT(24),
    var_b FLOAT(24),
    nick_nm TEXT ,
    link_img TEXT, 
    etq TEXT
    );


    ALTER TABLE public.ma_table DISABLE ROW LEVEL SECURITY;


    ALTER TABLE public.ma_table RENAME TO {};""".format(str(user))

    response = supabase.rpc("run_sql", {"script_sql": new_table}).execute()
    print("tableau perso ajouté", user)


def add_friend(usr, frd, bruit):
    data = supabase.table("user_database").select("*").eq('username', usr).single().execute()
    for i in data:
        for j in i:
            if isinstance(j, dict):
                lst_ami = j['lst_frd']
                lst_ami = lst_ami + str(frd) + ", "
                supabase.table("user_database").update({'lst_frd': lst_ami}).eq('username', usr).execute()
                msg = "tu as ajouté " + frd + "dans tes amis , recharge ton application pour voir ses :orange[reko]"
                if bruit is True:
                    st.markdown(msg)


def user_exist(nom):
    alrdused = 0
    data = supabase.table("user_database").select("*").execute()
    for i in data:
        if isinstance(i, tuple):
            for e in i:
                if isinstance(e, list):
                    for j in e:
                        if isinstance(j, dict):
                            if j['username'] == nom:
                                alrdused += 1
    if alrdused >= 1:
        return True
    else:
        return False


def deja_amis(usr, frd):
    dta = supabase.table("user_database").select('lst_frd').eq('username', usr).execute()
    lst_alrd = []
    frd = frd + ','
    for i in dta:
        for j in i:
            if isinstance(j, list):
                for k in j:
                    nom = ""
                    for e in k['lst_frd']:
                        nom = nom + e
                        if e == ',':
                            lst_alrd.append(nom)
                            nom = ""
    for am in lst_alrd:
        dmf = ' ' + am
        if am == frd:
            return True
        elif dmf == frd:
            return True
        else:
            pass
    return False


def ajt_reko(usr, titre, x, y, description):
    supabase.table(usr).insert({'nom': titre, 'var_a': x, 'var_b': y, 'nick_nm': description}).execute()
    pass


def get_lst_reko_ami(user):
    dta = supabase.table('user_database').select('lst_frd').eq('username', user).execute()
    lst = []
    bis = []
    for i in dta:
        for j in i:
            if isinstance(j, list):
                for k in j:
                    nom = ""
                    for e in k['lst_frd']:
                        nom = nom + e
                        if e == ',':
                            lst.append(nom)
                            nom = ""
    for i in lst:
        bis.append(i.replace(",",''))
    return bis



