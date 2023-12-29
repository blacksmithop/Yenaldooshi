import streamlit as st
from utils.wolvesville import Wolvesville
from utils.models import Backgrounds
from utils.helper import getTitle
from typing import List

api = Wolvesville()

screens: List[Backgrounds] = api.getBackgrounds()

st.markdown(getTitle("Backgrounds"), unsafe_allow_html=True)


for screen in screens[:5]:
    rarity = screen.rarity.title()
    st.header(rarity)
    dayCols = st.columns(3)
    dayCols[0].markdown(
        f'<img src="{screen.imageDay.url}" style="height:75%; width:75%;"/>',
        unsafe_allow_html=True,
    )
    dayCols[1].markdown(
        f'<img src="{screen.imageDaySmall.url}" style="height:75%; width:75%;"/>',
        unsafe_allow_html=True,
    )
    dayCols[2].markdown(
        f'<img src="{screen.imageDayWide.url}" style="height:75%; width:75%;"/>',
        unsafe_allow_html=True,
    )

    nightCols = st.columns(3)
    nightCols[0].markdown(
        f'<img src="{screen.imageNight.url}" style="height:75%; width:75%;"/>',
        unsafe_allow_html=True,
    )
    nightCols[1].markdown(
        f'<img src="{screen.imageNightSmall.url}" style="height:75%; width:75%;"/>',
        unsafe_allow_html=True,
    )
    nightCols[2].markdown(
        f'<img src="{screen.imageNightWide.url}" style="height:75%; width:75%;"/>',
        unsafe_allow_html=True,
    )
    st.divider()
