import streamlit as st
from utils.wolvesville import Wolvesville
from utils.models import LoadingScreen
from typing import List

api = Wolvesville()

screens: List[LoadingScreen] = api.getScreens()

st.title("Loading Screens")

for screen in screens[:5]:
    st.markdown(
        f'<img src="{screen.image.url}"  style="height:75%; width:75%;"/>',
        unsafe_allow_html=True,
    )

    rarity = screen.rarity.title()
    st.header(rarity)

    st.divider()
