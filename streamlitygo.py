from calendar import c
from contextlib import nullcontext
import streamlit as st
import plotly_express as px
import pandas as pd
from PIL import Image
import requests
import json


st.set_page_config(page_title="YGO Master Duel", page_icon=":flower_playing_cards:", layout="wide")

#header
image = Image.open('imgygo.jpg')
st.image(image,use_column_width=True)
st.subheader("Bonjour, bienvenue sur mon streamlit sur ygo")
st.title("YGO Master Duel Cards")
st.write("Vous retrouverez ici les différentes cartes monstres présentes sur ygo master duel.")

#sidebar

st.sidebar.subheader("Test")

#setup file upload
DATA_URL = ('http://127.0.0.1:80')

def load_data():
    data = pd.read_json(DATA_URL)
    return data

df = load_data()

st.dataframe(df)
#uploaded_file = st.sidebar.file_uploader(label="Upload csv", type=['csv'])
# res = requests.get("http://127.0.0.1:80")
#df = pd.read_csv(res)
#st.write(res.head(n=5))
# res = res.json()
# st.dataframe(res)
# data = json.load(res)
# st.dataframe(data['ATK'])
# global df
# if uploaded_file is not None:
    # df = pd.read_csv(uploaded_file)

#  try:
#      #st.write(df)
#      dfbase = df
#      st.dataframe(df)
#  except:
#      st.write("No data found")
dfbase = df

with st.sidebar.form(key = "form1"):
    cardname = st.text_input(label="Nom de la carte:")
    submit1 = st.form_submit_button(label = "Submit")

with st.sidebar.form(key = "form2"):
    type = st.text_input(label="Type de la carte:")
    submit2 = st.form_submit_button(label = "Submit")

with st.sidebar.form(key = "form3"):
    attaque = st.slider("Tri par attaque", min_value=0, max_value=10000, value=10000)
    submit3 = st.form_submit_button(label = "Submit")


with st.sidebar.form(key = "form4"):
    defense = st.slider("Tri par défense", min_value=0, max_value=10000, value=10000)
    submit4 = st.form_submit_button(label = "Submit")

with st.sidebar.form(key = "form5"):
     
    # element = st.text_input(label="Tri par élément, précisez l'élément voulu:")
    # submit5 = st.form_submit_button(label = "Submit")
    element = st.selectbox('Préciser un élément',('','LIGHT', 'DARK', 'EARTH', 'WIND', 'FIRE', 'WATER', 'DIVINE'))
    submit5 = st.form_submit_button(label = "Submit")
    # st.write('You selected:', element)

with st.sidebar.form(key = "form6"):
    descri = st.text_input(label="Texte de description:")
    submit6 = st.form_submit_button(label = "Submit")

# with st.sidebar.form(key = "form7"):
#     submit7 = st.form_submit_button(label = "Reset")
#     if submit7:
#         dfbase = df
#         cardname = st.text_input(label="Nom de la carte:")
#         type = st.text_input(label="type de la carte:")
#         attaque = None
#         defense = None
#         element = None

df_filtred = dfbase.loc[(dfbase["Card Name"].str.contains(cardname)) 
    & (dfbase["Type"].str.contains(type)
    & (dfbase["ATK"] <= attaque)
    & (dfbase["DEF"] <= defense)
    & (dfbase["Element"].str.contains(element))
    & (dfbase["Description"].str.contains(descri))
    )] 
st.dataframe(df_filtred)

# if submit1:
#     dfbase = dfbase[dfbase["Card Name"].str.contains(cardname)]
#     st.write(dfbase)

# if submit2:
#     dfbase = dfbase[dfbase["Type"].str.contains(type)]
#     st.write(dfbase)

# if submit3:
#     dfbase = dfbase.loc[df["ATK"] <= attaque]
#     st.write(dfbase)

# if submit4:
#     dfbase = dfbase.loc[dfbase["DEF"] <= defense]
#     st.write(dfbase)

# if submit5:
#     dfbase = dfbase[dfbase["Element"].str.contains(element)]
#     st.write(dfbase)

# if submit6:
#     dfbase = dfbase[dfbase["Description"].str.contains(descri)]
#     st.write(dfbase)





