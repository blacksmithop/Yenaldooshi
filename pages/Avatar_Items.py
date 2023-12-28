import streamlit as st
from utils.wolvesville import Wolvesville
from utils.models import AvatarItems
from typing import List

api = Wolvesville()

items: List[AvatarItems] = api.getItems()

st.title("Avatar Items")

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
