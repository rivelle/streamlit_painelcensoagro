import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
import folium.features
from streamlit_folium import st_folium
from utils import formatar_numeros


st.set_page_config(layout = 'wide')
st.title('Painel Geral')

# DADOS

mun_geo = gpd.read_file('basedados/base_limites_municipios2022.geojson')
mun_geo_pts = gpd.read_file('basedados/base_centroides_municipios2022.geojson')
mun_csv = pd.read_csv('basedados/base_municipios2022.csv')



mun_csv = mun_csv.rename(columns = {'NM_MUN': 'Município', 
                                    'TER_IDENT': 'Território', 
                                    'est_agrico': 'Estabelecimentos Agropecuarios', 
                                    'est_agricf': 'Estabelecimentos Familiares', 'biomapredo': 'Bioma'})

# FILTROS

territorio = st.sidebar.selectbox('Filtro por Território', sorted(mun_csv['Território'].unique()), index = None, placeholder = 'Selecione o Território')
bioma = st.sidebar.selectbox('Filtro por Bioma', sorted(mun_csv['Bioma'].unique()), index = None, placeholder = 'Selecione o Bioma')
municipio = st.sidebar.selectbox('Filtro por Município', sorted(mun_csv['Município'].unique()), index = None, placeholder = 'Selecione o Município')


if territorio:
    mun_csv = mun_csv[mun_csv['Território'] == territorio]
if territorio:
    mun_geo = mun_geo[mun_geo['ter_ident'] == territorio]


if bioma:
    mun_csv = mun_csv[mun_csv['Bioma'] == bioma]
if bioma:
    mun_geo = mun_geo[mun_geo['biomapredo'] == bioma]

if municipio:
    mun_csv = mun_csv[mun_csv['Município'] == municipio]
if municipio:
    mun_geo = mun_geo[mun_geo['nm_mun'] == municipio]


# MAPA


def mapa_geral(geojson):

    mapa_estab_af = folium.Map(['-13.528483', '-41.201439'], zoom_start = 6.5)

    folium.Choropleth(mun_geo, 
                    data=mun_csv, 
                    columns=["Município", "Estabelecimentos Familiares"], 
                    key_on="feature.properties.nm_mun", 
                    fill_color='OrRd',
                    legend_name='Número de Estabelecimentos Familiares').add_to(mapa_estab_af)

    estilo = lambda x: {
        "fillColor": "white",
        "color": "black",
        "fillOpacity": 0.001,
        "weight": 0.001}

    estilo_destaque = lambda x: {"fillColor": "darkblue",
                                "color": "black",
                                "fillOpacity": 0.5,
                                "weight": 1}

    highlight = folium.features.GeoJson(data=mun_geo,
                                        style_function=estilo,
                                        highlight_function=estilo_destaque)

    folium.features.GeoJsonTooltip(fields=["nm_mun", "ter_ident", "est_agrico", "est_agricf", "biomapredo"],
                                aliases=["Município", "Território", "Estabelecimentos Agropecuários", "Estabelecimentos Familiares", "Bioma"]).add_to(highlight)

    mapa_estab_af.add_child(highlight)

    st_map = st_folium(mapa_estab_af, width=1000, height=1000)



# DISPLAY

st.header('Caracterização Geral Agricultura Familiar')


col01, col02 = st.columns(2)

with col01:
    st.metric('Estabelecimentos Agropecuários', formatar_numeros(mun_csv['Estabelecimentos Agropecuarios'].sum()))
    st.metric('Estabelecimentos da Agricultura Familiar', formatar_numeros(mun_csv['Estabelecimentos Familiares'].sum()))
    st.metric('Número de Municípios', mun_csv.shape[0])

    st.dataframe(mun_csv[['Município', 'Território', 'Estabelecimentos Agropecuarios', 'Estabelecimentos Familiares']], hide_index=True)
    st.write(mun_csv.shape)
    st.bar_chart(mun_csv,
                 x = "Território",
                 x_label = "Estabelecimentos Agropecuários e Estabelecimentos da Agricultura Familiar",
                 y = ["Estabelecimentos Agropecuarios", "Estabelecimentos Familiares"],
                 y_label = "Território de Identidade",
                 stack = False,
                 use_container_width = True
                 )

    st.bar_chart(mun_csv,
                 x = "Bioma",
                 x_label = "Estabelecimentos Agropecuários e Estabelecimentos da Agricultura Familiar",
                 y = ["Estabelecimentos Agropecuarios", "Estabelecimentos Familiares"],
                 y_label = "Bioma Presente",
                 stack = False,
                 use_container_width = True
                )

    
with col02:
    mapa_geral(mun_geo)
    
    


    




    




    


