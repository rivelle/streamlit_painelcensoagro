import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
import folium.features
from streamlit_folium import st_folium
from utils import formatar_numeros


st.set_page_config(layout = 'wide')
st.title('Painel Sistemas Produtivos')

mun_geo = gpd.read_file('/home/rivelle/01-ZNTGEO/00-Projetos/2403-DSP/basedados/base_limites_municipios2022.geojson')
pec_csv = pd.read_csv('/home/rivelle/01-ZNTGEO/00-Projetos/2403-DSP/basedados/pecuaria_bahia.csv')

tab01, tab02 = st.tabs(['Agricultura', 'Pecuária'])



with tab01:

    st.header('Produção Agrícola na Bahia - Censo Agropecuário | IBGE 2017')

    # FILTROS

    # territorio = st.sidebar.selectbox('Filtro por Território', sorted(pec_csv['territorio'].unique()), index = None, placeholder = 'Selecione o Território')
    # bioma = st.sidebar.selectbox('Filtro por Bioma', sorted(pec_csv['biomapredo'].unique()), index = None, placeholder = 'Selecione o Bioma')
    municipio = st.sidebar.selectbox('Filtro por Município', sorted(pec_csv['nm_mun'].unique()), index = None, placeholder = 'Selecione o Município')

    # if territorio:
    #     mun_csv = pec_csv[pec_csv['territorio'] == territorio]
    # if territorio:
    #     mun_geo = mun_geo[mun_geo['TER_IDENT'] == territorio]


    # if bioma:
    #     mun_csv = pec_csv[pec_csv['biomapredo'] == bioma]
    # if bioma:
    #     mun_geo = mun_geo[mun_geo['biomapredo'] == bioma]

    if municipio:
        mun_csv = pec_csv[pec_csv['nm_mun'] == municipio]
    if municipio:
        mun_geo = mun_geo[mun_geo['NM_MUN'] == municipio]


    # Funções


    def mapa_geral(geojson):
        pass

       
    # DISPLAY


    st.header('Caracterização Geral Agricultura Familiar')


    col01, col02 = st.columns(2)

    with col01:
        st.metric('Estabelecimentos Agropecuários', formatar_numeros(pec_csv['nfam_estab'].sum()))
        st.metric('Estabelecimentos da Agricultura Familiar', formatar_numeros(pec_csv['fam_estab'].sum()))
        st.metric('Número de Municípios', pec_csv.shape[0])
        st.write(pec_csv)
        st.write(pec_csv.shape)
        # st.bar_chart(pec_csv,
        #             x = "TER_IDENT",
        #             x_label = "Esatbelecimentos Agropecuários e Estabelecimentos da Agricultura Familiar",
        #             y = ["est_agrico", "est_agricf"],
        #             y_label = "Território de Identidade",
        #             stack = False,
        #             use_container_width = True
        #             )

        # st.bar_chart(mun_csv,
        #             x = "biomapredo",
        #             x_label = "Esatbelecimentos Agropecuários e Estabelecimentos da Agricultura Familiar",
        #             y = ["est_agrico", "est_agricf"],
        #             y_label = "Bioma Presente",
        #             stack = False,
        #             use_container_width = True
        #             )

        
        
    with col02:
        mapa_geral(mun_geo)


    with tab02:

        st.header('Produção Pecuária na Bahia - Censo Agropecuário | IBGE 2017')