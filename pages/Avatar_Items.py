import streamlit as st
from utils.wolvesville import Wolvesville
from utils.models import AvatarItems, AvatarItemSets
from utils.helper import getTitle
from typing import List

api = Wolvesville()

items: List[AvatarItems] = api.getItems()
itemSets: List[AvatarItemSets] = api.getItemAsSets()

st.markdown(getTitle("Avatar Items"), unsafe_allow_html=True)

for item in items[:5]:
    st.markdown(
        f'<img src="{item.imageUrl}" style="height: 100px; width:100px;"/>',
        unsafe_allow_html=True,
    )

    itemType = item.type.title()
    st.subheader(itemType)
    rarity = item.rarity.title()
    st.markdown(rarity)
    st.button(f"{item.costInGold} 🪙", key=item.id)

    st.divider()

st.markdown(getTitle("Item Collections"), unsafe_allow_html=True)
for item in itemSets[:5]:
    st.markdown(
        f'<img src="{item.promoImageUrl}" style="height: 75%; width:75%;"/>',
        unsafe_allow_html=True,
    )

    if item.ids != []:
        with st.expander("See item sets"):
            for id in item.ids:
                st.markdown(
                    f'<img src="{id}" style="height: 25%; width:25%;"/>',
                    unsafe_allow_html=True,
                )

    st.divider()
