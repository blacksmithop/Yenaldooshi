import streamlit as st
from utils.wolvesville import Wolvesville
from utils.helper import getTitle


st.set_page_config(layout="wide")

api = Wolvesville()

st.markdown(getTitle("Wolvesville App"), unsafe_allow_html=True)
