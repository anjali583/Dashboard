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

st.write('# :green[TRANSACTIONS ANALYSIS]')
Data_Aggregated_Transaction=Data_Aggregated_Transaction_df.copy()
Data_Aggregated_Transaction.drop(Data_Aggregated_Transaction.index[(Data_Aggregated_Transaction["State"] == "india")],axis=0,inplace=True)
State_PaymentMode=Data_Aggregated_Transaction.copy()
st.write('### :green[State & PaymentMode]')
col1, col2= st.columns(2)
with col1:
        mode = st.selectbox(
            'Please select the Mode',
            ('Recharge & bill payments', 'Peer-to-peer payments', 'Merchant payments', 'Financial Services','Others'),key='a')
with col2:
        state = st.selectbox(
        'Please select the State',
        ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
        'assam', 'bihar', 'chandigarh', 'chhattisgarh',
        'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
        'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
        'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
        'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
        'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
        'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
        'uttarakhand', 'west-bengal'),key='b')
State= state
Year_List=[2018,2019,2020,2021,2022]
Mode=mode
State_PaymentMode=State_PaymentMode.loc[(State_PaymentMode['State'] == State ) & (State_PaymentMode['Year'].isin(Year_List)) & 
                            (State_PaymentMode['Payment_Mode']==Mode )]
State_PaymentMode = State_PaymentMode.sort_values(by=['Year'])
State_PaymentMode["Quarter"] = "Q"+State_PaymentMode['Quarter'].astype(str)
State_PaymentMode["Year_Quarter"] = State_PaymentMode['Year'].astype(str) +"-"+ State_PaymentMode["Quarter"].astype(str)
fig = px.bar(State_PaymentMode, x='Year_Quarter', y='Total_Transactions_count',color="Total_Transactions_count",
                 color_continuous_scale="Viridis")
    
colT1,colT2 = st.columns([7,3])
with colT1:
        st.write('#### '+State.upper()) 
        st.plotly_chart(fig,use_container_width=True)
with colT2:
        st.info(
        """
        Details of BarGraph:
        - This entire data belongs to state selected by you
        - X Axis is basically all years with all quarters 
        - Y Axis represents total transactions in selected mode        
        """
        )
        st.info(
        """
        Important Observations:
        - User can observe the pattern of payment modes in a State 
        - We get basic idea about which mode of payments are either increasing or decreasing in a state
        """
        )
        
