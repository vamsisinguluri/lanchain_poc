import streamlit as st
import helper

st.title("Weather Bot with LLM and Streamlit 🌤️")

city = st.text_input("Enter the city name:")

if st.button("Get Weather"):
    if city:
        # Call SequentialChain
        output = helper.chain({"city": city})
        st.write("Result:", output['weather_info'])
    else:
        st.warning("Please enter a city name.")
