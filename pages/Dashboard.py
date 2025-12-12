import streamlit as st
from app.incidents import migrating_cyber_incidents
from app.db import get_db_connection


st.header('Cyber Incidents Dashboard')
st.write('Welcome to the Home Page of the Application!')

st.set_page_config(
    page_title="Home Page",
    page_icon="🏠",
    layout="wide"
)

conn = get_db_connection()
data = migrating_cyber_incidents(conn)

with st.sidebar:
    st.header('Cyber Incidents Overview')
    severity_ = st.selectbox('severity', data['severity'].unique())

filtered_data = data[data['severity'] == severity_]

col1, col2 = st.columns(2)
with col1:
    st.subheader('Number of Incidents by Severity')
    st.bar_chart(filtered_data['category'].value_counts())

with col2:
    st.subheader('Filtered Cyber Incidents Data')
    st.line_chart(filtered_data, x='timestamp', y='incident_id')
st.dataframe(filtered_data) 