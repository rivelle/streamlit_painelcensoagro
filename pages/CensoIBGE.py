import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
import folium.features
from streamlit_folium import st_folium
from utils import formatar_numeros


st.set_page_config(layout = 'wide')
st.title('Painel Sistemas Produtivos')

mun_geo = gpd.read_file('basedados/base_limites_municipios2022.geojson')
pec_csv = pd.read_csv('basedados/base_mun_pecuaria_bahia.csv')



tab01, tab02 = st.tabs(['Pecuária', 'Agricultura'])


with tab01:

    st.header('Produção Pecuária na Bahia - Censo Agropecuário | IBGE 2017')

    

    # FILTROS

    sisprod = st.sidebar.selectbox('Filtro por Sistema Produtivo', sorted(pec_csv['sisprod'].unique()), index = None, placeholder = 'Selecione o Sistema Produtivo')

    territorio = st.sidebar.selectbox('Filtro por Território', sorted(pec_csv['ter_ident'].unique()), index = None, placeholder = 'Selecione o Território')
    bioma = st.sidebar.selectbox('Filtro por Bioma', sorted(pec_csv['biomapredo'].unique()), index = None, placeholder = 'Selecione o Bioma')
    municipio = st.sidebar.selectbox('Filtro por Município', sorted(pec_csv['nm_mun'].unique()), index = None, placeholder = 'Selecione o Município')

    if sisprod:
        pec_csv = pec_csv[pec_csv['sisprod'] == sisprod]
    
    if territorio:
        pec_csv = pec_csv[pec_csv['ter_ident'] == territorio]

    if bioma:
        pec_csv = pec_csv[pec_csv['biomapredo'] == bioma]

    if municipio:
        pec_csv = pec_csv[pec_csv['nm_mun'] == municipio]


    st.metric(f"Estabelecimentos Familiares com Produção Pecuária {sisprod}", formatar_numeros(pec_csv['fam_estab'].sum()))
    st.metric(f"Número de Animais da Agricultura Familiar", formatar_numeros(pec_csv['fam_animais'].sum()))

    st.write(pec_csv)
    st.write(pec_csv.shape)

    