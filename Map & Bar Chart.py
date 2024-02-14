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


colT1,colT2 = st.columns([2,8])
with colT2:
    st.title(':blue[PhonePe Data Analysis:signal_strength:]')
c1,c2=st.columns(2)
with c1:
    Year = st.selectbox(
            'Please select the Year',
            ('2018', '2019', '2020','2021','2022'))
with c2:
    Quarter = st.selectbox(
            'Please select the Quarter',
            ('1', '2', '3','4'))
    
year=int(Year)
quarter=int(Quarter)
Transaction_scatter_districts=Data_Map_Transaction_df.loc[(Data_Map_Transaction_df['Year'] == year ) & (Data_Map_Transaction_df['Quarter']==quarter) ].copy()
Transaction_Coropleth_States=Transaction_scatter_districts[Transaction_scatter_districts["State"] == "india"]
Transaction_scatter_districts.drop(Transaction_scatter_districts.index[(Transaction_scatter_districts["State"] == "india")],axis=0,inplace=True)
Transaction_scatter_districts = Transaction_scatter_districts.sort_values(by=['Place_Name'], ascending=False)
Scatter_Geo_Dataset = Scatter_Geo_Dataset.sort_values(by=['District'], ascending=False) 
Total_Amount=[]
for i in Transaction_scatter_districts['Total_Amount']:
    Total_Amount.append(i)
Scatter_Geo_Dataset['Total_Amount']=Total_Amount
Total_Transaction=[]
for i in Transaction_scatter_districts['Total_Transactions_count']:
    Total_Transaction.append(i)
Scatter_Geo_Dataset['Total_Transactions']=Total_Transaction
Scatter_Geo_Dataset['Year_Quarter']=str(year)+'-Q'+str(quarter)
Coropleth_Dataset = Coropleth_Dataset.sort_values(by=['state'], ascending=False)
Transaction_Coropleth_States = Transaction_Coropleth_States.sort_values(by=['Place_Name'], ascending=False)
Total_Amount=[]
for i in Transaction_Coropleth_States['Total_Amount']:
    Total_Amount.append(i)
Coropleth_Dataset['Total_Amount']=Total_Amount
Total_Transaction=[]
for i in Transaction_Coropleth_States['Total_Transactions_count']:
    Total_Transaction.append(i)
Coropleth_Dataset['Total_Transactions']=Total_Transaction

Indian_States = Indian_States.sort_values(by=['state'], ascending=False)
Indian_States['Registered_Users']=Coropleth_Dataset['Registered_Users']
Indian_States['Total_Amount']=Coropleth_Dataset['Total_Amount']
Indian_States['Total_Transactions']=Coropleth_Dataset['Total_Transactions']
Indian_States['Year_Quarter']=str(year)+'-Q'+str(quarter)
fig=px.scatter_geo(Indian_States,
                    lon=Indian_States['Longitude'],
                    lat=Indian_States['Latitude'],                                
                    text = Indian_States['code'], #It will display district names on map
                    hover_name="state", 
                    hover_data=['Total_Amount',"Total_Transactions","Year_Quarter"],
                    )
fig.update_traces(marker=dict(color="white" ,size=0.3))
fig.update_geos(fitbounds="locations", visible=False,)
    # scatter plotting districts
Scatter_Geo_Dataset['col']=Scatter_Geo_Dataset['Total_Transactions']
fig1=px.scatter_geo(Scatter_Geo_Dataset,
                    lon=Scatter_Geo_Dataset['Longitude'],
                    lat=Scatter_Geo_Dataset['Latitude'],
                    color=Scatter_Geo_Dataset['col'],
                    size=Scatter_Geo_Dataset['Total_Transactions'],     
                    #text = Scatter_Geo_Dataset['District'], #It will display district names on map
                    hover_name="District", 
                    hover_data=["State", "Total_Amount","Total_Transactions","Year_Quarter"],
                    title='District',
                    size_max=22,)
fig1.update_traces(marker=dict(color="rebeccapurple" ,line_width=1))    #rebeccapurple
#coropleth mapping india
fig_ch = px.choropleth(
                    Coropleth_Dataset,
                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',                
                    locations='state',
                    color="Total_Transactions",                                       
                    )
fig_ch.update_geos(fitbounds="locations", visible=False,)
#combining districts states and coropleth
fig_ch.add_trace( fig.data[0])
fig_ch.add_trace(fig1.data[0])
st.write("### **:black[PhonePe India Map]**")
colT1,colT2 = st.columns([6,4])
with colT1:
    st.plotly_chart(fig_ch, use_container_width=True)
with colT2:
    st.info(
    """
    Details of Map:
    - The darkness of the state color represents the total transactions
    - The Size of the Circles represents the total transactions dictrict wise
    - The bigger the Circle the higher the transactions
    - Hover data will show the details like Total transactions, Total amount
    """
    )
    st.info(
    """
    Important Observations:
    - User can observe Transactions of PhonePe in both statewide and Districtwide.
    - We can clearly see the states with highest transactions in the given year and quarter
    - We get basic idea about transactions district wide
    """
    )
###############################################
st.divider()  
Coropleth_Dataset = Coropleth_Dataset.sort_values(by=['Total_Transactions'])
fig = px.bar(Coropleth_Dataset, x='state', y='Total_Transactions',title=str(year)+" Quarter-"+str(quarter))
with st.expander("See Bar graph for the same data"):
     st.plotly_chart(fig, use_container_width=True)
st.info('**:blue[The above bar graph showing the increasing order of PhonePe Transactions according to the states of India, Here we can observe the top states with highest Transaction by looking at graph]**')
