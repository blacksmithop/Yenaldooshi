import streamlit as st
from utils.wolvesville import Wolvesville
from utils.models import Role
from typing import List

api = Wolvesville()

roles: List[Role] = api.getRoleRoleIcons()

st.title("Roles")

for role in roles[:5]:
    st.markdown(
        f'<img src="{role.image.url}" style="height: 100px; width:100px;"/>',
        unsafe_allow_html=True,
    )

    st.subheader(role.name)
    aura = role.aura.title()
    st.markdown(aura)
    st.markdown(role.description)

    if role.icons != []:
        with st.expander("See role icons"):
            for icon in role.icons:
                st.markdown(
                    f'<img src="{icon}" style="height: 100px; width:100px;"/>',
                    unsafe_allow_html=True,
                )

    st.divider()
