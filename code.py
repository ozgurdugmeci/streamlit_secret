import streamlit as st

# Everything is accessible via the st.secrets dict:

st.write("consumer_key:", st.secrets["consumer_key"])
