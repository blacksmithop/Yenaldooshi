import streamlit as st
from utils.wolvesville import Wolvesville
from utils.models import Role
from utils.helper import chunks, getTitle
from typing import List

api = Wolvesville()

roles: List[Role] = api.getRoleRoleIcons()

st.markdown(getTitle("Roles"), unsafe_allow_html=True)
st.divider()

CHUNK_SIZE = 4

for roles in chunks(roles, CHUNK_SIZE):
    cols = st.columns(CHUNK_SIZE)
    for role, col in zip(roles, cols):
        col.markdown(
            f'<img src="{role.image.url}" style="height: 100px; width:100px;"/>',
            unsafe_allow_html=True,
        )

        col.subheader(role.name)
        aura = role.aura.title()
        col.markdown(aura)
        col.markdown(role.description)

        if role.icons != []:
            icons = role.icons
            with st.expander(f"See {role.name} icons"):
                cols = st.columns(len(icons))
                for icon, col in zip(icons, cols):
                    col.markdown(
                        f'<img src="{icon}" style="height: 100px; width:100px;"/>',
                        unsafe_allow_html=True,
                    )

    st.divider()
