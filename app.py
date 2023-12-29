import streamlit as st
from utils.wolvesville import Wolvesville
from utils.helper import getTitle


api = Wolvesville()

st.markdown(getTitle("Wolvesville App"), unsafe_allow_html=True)
