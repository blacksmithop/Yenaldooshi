import streamlit as st
from utils.wolvesville import Wolvesville
from utils.models import AvatarItems, AvatarItemSets
from utils.helper import chunks, getTitle, groupItemCategories
from typing import List

api = Wolvesville()

_items: List[AvatarItems] = api.getItems()
itemGroup = groupItemCategories(items=_items)

itemAvatarSets: List[AvatarItemSets] = api.getItemAsSets()

st.markdown(getTitle("Avatar Items"), unsafe_allow_html=True)

CHUNK_SIZE = 4

for itemType, itemSets in itemGroup.items():
    itemType = itemType.title()
    with st.expander(f"See {itemType}"):
        for items in chunks(itemSets[:8], CHUNK_SIZE):
            cols = st.columns(CHUNK_SIZE)
            for item, col in zip(items, cols):
                col.markdown(
                    f'<img src="{item.imageUrl}" style="height: 100px; width:100px;"/>',
                    unsafe_allow_html=True,
                )
                rarity = item.rarity.title()
                col.markdown(rarity)
                col.button(f"{item.costInGold} 🪙", key=item.id)

                col.divider()

st.markdown(getTitle("Item Collections"), unsafe_allow_html=True)
for item in itemAvatarSets:
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
