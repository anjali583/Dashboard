import streamlit as st 
import warnings
warnings.filterwarnings("ignore")
st.set_page_config(layout="wide")

with st.markdown('PhonePe Dashboard'):
    st.title(':blue[PhonePe Data Analysis:signal_strength:]')
colT1,colT2 = st.columns([6,5])
with colT1:
    st.image("Make.png")
with colT2:
    st.info(
    """
    Objectives:
    - Enable users to visually explore PhonePe transactions across India by offering interactive maps with a focus on user-specified years and quarters.
    - Analyze PhonePe transaction data by payment modes to understand user preferences and optimize payment services strategically.
    - To assist stakeholders in identifying impactful regions for strategic decision-making, compile the most important indicators for high-performing states.
    - Provide visual insights into PhonePe transactions, allowing users to analyze types, amounts, and timelines for informed decision-making.
    """
    )
    

