import streamlit as st
from utils.helper import chunks, getTitle
from utils.models import AdvancedRoleCardOffers
from utils.wolvesville import Wolvesville
from typing import List
from uuid import uuid4


api = Wolvesville()

offerList: List[AdvancedRoleCardOffers] = api.getRoleCardOffers()

CHUNK_SIZE = 4


st.markdown(getTitle("Role Card Offers"), unsafe_allow_html=True)

for roles in chunks(offerList, CHUNK_SIZE):
    cols = st.columns(CHUNK_SIZE)
    for role, col in zip(roles, cols):
        col.markdown(
            f'<img src="{role.promoImageUrl}" style="height: 75%; width:75%;"/>',
            unsafe_allow_html=True,
        )

        advancedRoleId = role.advancedRoleId
        advancedRoleId = " ".join(advancedRoleId.split("-"))
        col.subheader(advancedRoleId)
        col.button(f"Ability exchange vouchers: {role.abilityExchangeVoucherCount}", key=uuid4().hex)
        col.button(f"Talismans: {role.talismanCount}", key=uuid4().hex)
        col.button(f"Loyalty Tokens: {role.loyaltyTokenCount}", key=uuid4().hex)

    st.divider()

st.toast("Loaded offers", icon="💰")
