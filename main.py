"""

    install streamlit

"""

import streamlit as st
import lanchain_helper



st.title("Restaurant Name Generator")


country = st.sidebar.selectbox("Pick a country", ("indin", "Mexio", "Italian", "Arabic"))


if country:
    response = lanchain_helper.generate_restaurant_name_and_items(country)
    st.header(response['restaurant_name'].strip())
    menu_items = response["menu_items"].strip().split(",")
    st.write("**Menu Items**")

    for item in menu_items:
        st.write("-", item)





