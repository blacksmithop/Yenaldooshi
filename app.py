import streamlit as st
from utils.wolvesville import Wolvesville
from utils.models import Role
from typing import List

api = Wolvesville()

roles: List[Role] = api.getRoleRoleIcons()
for role in roles[:5]:
    st.markdown(f"<img src=\"{role.image.url}\" style=\"height: 100px; width:100px;\"/>", unsafe_allow_html=True)
    