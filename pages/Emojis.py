import streamlit as st
from utils.wolvesville import Wolvesville
from utils.models import Emoji, EmojiCollection
from typing import List

api = Wolvesville()

collections: List[EmojiCollection] = api.getEmojiAsCollections()
emojis: List[Emoji] = api.getEmojis()

st.header("Emojis")

for emoji in emojis[:5]:
    st.subheader(emoji.name.title())
    st.markdown(emoji.rarity.title())
    st.markdown(
        f'<img src="{emoji.urlPreview}" style="height: 100px; width:100px;"/>',
        unsafe_allow_html=True,
    )
    st.markdown(f"Event: {emoji.event.title() if emoji.event else 'None'}")

st.header("Emoji Collections")

for item in collections[:5]:
    st.markdown(
        f'<img src="{item.promoImageUrl}" style="height: 75%; width:75%;"/>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<img src="{item.iconUrl}" style="height: 100px; width:100px;"/>',
        unsafe_allow_html=True,
    )
    if item.emojis != []:
        with st.expander("See role icons"):
            for emoji in item.emojis[:5]:
                name = emoji.name.title()
                name = " ".join(name.split("_"))
                st.subheader(name)
                st.markdown(emoji.rarity.title())
                st.markdown(
                    f'<img src="{emoji.urlPreview}" style="height: 100px; width:100px;"/>',
                    unsafe_allow_html=True,
                )
                eventName = emoji.event.title() if emoji.event else "None"
                eventName = " ".join(eventName.split("_"))
                st.markdown(f"Event: {eventName}")
    st.divider()
