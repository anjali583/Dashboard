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

st.write('### :blue[Payment Mode and Year]')
Data_Aggregated_Transaction=Data_Aggregated_Transaction_df.copy()
col1, col2= st.columns(2)
with col1:
        M = st.selectbox(
            'Please select the Mode',
            ('Recharge & bill payments', 'Peer-to-peer payments', 'Merchant payments', 'Financial Services','Others'),key='D')
with col2:
        Y = st.selectbox(
        'Please select the Year',
        ('2018', '2019', '2020','2021','2022'),key='F')
Year_PaymentMode=Data_Aggregated_Transaction.copy()
Year=int(Y)
Mode=M
Year_PaymentMode=Year_PaymentMode.loc[(Year_PaymentMode['Year']==Year) & 
                            (Year_PaymentMode['Payment_Mode']==Mode )]
States_List=Year_PaymentMode['State'].unique()
State_groupby_YP=Year_PaymentMode.groupby('State')
Year_PaymentMode_Table=State_groupby_YP.sum()
Year_PaymentMode_Table['states']=States_List
del Year_PaymentMode_Table['Quarter'] # ylgnbu', 'ylorbr', 'ylorrd teal
del Year_PaymentMode_Table['Year']
Year_PaymentMode_Table = Year_PaymentMode_Table.sort_values(by=['Total_Transactions_count'])
fig2= px.bar(Year_PaymentMode_Table, x='states', y='Total_Transactions_count',color="Total_Transactions_count",
                color_continuous_scale="Viridis",)   
colT1,colT2 = st.columns([7,3])
with colT1:
        st.write('#### '+str(Year)+' DATA ANALYSIS')
        st.plotly_chart(fig2,use_container_width=True) 
with colT2:
        st.info(
        """
        Details of BarGraph:
        - This entire data belongs to selected Year
        - X Axis is all the states in increasing order of Total transactions
        - Y Axis represents total transactions in selected mode        
        """
        )
        st.info(
        """
        Important Observations:
        - We can observe the leading state with highest transactions in particular mode
        - We get basic idea about regional performance of Phonepe
        - Depending on the regional performance Phonepe can provide offers to particular place
        """
        )