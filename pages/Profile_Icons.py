import streamlit as st
from utils.wolvesville import Wolvesville
from utils.models import ProfileIcons
from typing import List

api = Wolvesville()


css_example = '''                                                                                                                                                  
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">                                                                                                    
'''
st.write(css_example, unsafe_allow_html=True)


icons: List[ProfileIcons] = api.getProfileIcons()


for item in icons:
    rarity = item.rarity.title()
    HTML = f"<p><i class=\"fas fa-{item.name} fa-2xl\"></i> {rarity}</p>"
    st.write(HTML, unsafe_allow_html=True)

    st.divider()