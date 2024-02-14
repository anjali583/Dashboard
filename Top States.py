import pandas as pd 
import plotly.express as px
import streamlit as st 
import warnings
import plotly.graph_objects as go
from plotly.subplots import make_subplots
warnings.filterwarnings("ignore")
st. set_page_config(layout="wide")

Data_Aggregated_Transaction_df= pd.read_csv('Data_Aggregated_Transaction_Table.csv')
Data_Aggregated_User_Summary_df= pd.read_csv('Data_Aggregated_User_Summary_Table.csv')
Data_Aggregated_User_df= pd.read_csv('Data_Aggregated_User_Table.csv')
Scatter_Geo_Dataset =  pd.read_csv('Data_Map_Districts_Longitude_Latitude.csv')
Coropleth_Dataset =  pd.read_csv('Data_Map_IndiaStates_TU.csv')
Data_Map_Transaction_df = pd.read_csv('Data_Map_Transaction_Table.csv')
Data_Map_User_Table= pd.read_csv('Data_Map_User_Table.csv')
Indian_States= pd.read_csv('Longitude_Latitude_State_Table.csv')

st.write('# :red[TOP 3 STATES DATA]')
c1,c2=st.columns(2)
with c1:
    Year = st.selectbox(
            'Please select the Year',
            ('2022', '2021','2020','2019','2018'),key='y1h2k')
with c2:
    Quarter = st.selectbox(
            'Please select the Quarter',
            ('1', '2', '3','4'),key='qgwe2')
Data_Map_User_df=Data_Aggregated_User_Summary_df.copy() 
top_states=Data_Map_User_df.loc[(Data_Map_User_df['Year'] == int(Year)) & (Data_Map_User_df['Quarter'] ==int(Quarter))]
top_states_r = top_states.sort_values(by=['Registered_Users'], ascending=False)
top_states_a = top_states.sort_values(by=['AppOpenings'], ascending=False) 

top_states_T=Data_Aggregated_Transaction_df.loc[(Data_Aggregated_Transaction_df['Year'] == int(Year)) & (Data_Aggregated_Transaction_df['Quarter'] ==int(Quarter))]
topst=top_states_T.groupby('State')
x=topst.sum().sort_values(by=['Total_Transactions_count'], ascending=False)
y=topst.sum().sort_values(by=['Total_Amount'], ascending=False)
col1, col2, col3, col4= st.columns([2.5,2.5,2.5,2.5])
with col1:
    rt=top_states_r[1:4]
    st.markdown("#### :blue[Registered Users :bust_in_silhouette:]")
    st.markdown(rt[[ 'State','Registered_Users']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
with col2:
    at=top_states_a[1:4]
    st.markdown("#### :blue[PhonePeApp Openings:iphone:]")
    st.markdown(at[['State','AppOpenings']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
with col3:
    st.markdown("#### :blue[Total Transactions:currency_exchange:]")
    st.write(x[['Total_Transactions_count']][1:4])
with col4:
    st.markdown("#### :blue[Total Amount :dollar:]")
    st.write(y['Total_Amount'][1:4])      