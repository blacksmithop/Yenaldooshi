import streamlit as st
from utils.wolvesville import Wolvesville
from utils.helper import getTitle


api = Wolvesville()

st.markdown(getTitle("Yenaldooshi"), unsafe_allow_html=True)
