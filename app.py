import streamlit as st
import requests

st.set_page_config(
    page_title="Fact Fizz",
    page_icon="icon.png",
    menu_items={
        "About":"Dive into FactFizz, where every click uncovers a fresh and intriguing fact! Perfect for sparking curiosity and adding a dose of wonder to your day, FactFizz delivers a new random fact instantly, keeping you engaged and enlightened with each visit."
    }
)

st.write("<h2 style='color:#B4E380;font-size:30px;'>Uncover a Fascinating Fact with Every Click!</h2>",unsafe_allow_html=True)

btn=st.button("Generate")
if btn:
    try:
        api_url = 'https://api.api-ninjas.com/v1/facts?'
        response = requests.get(api_url, headers={'X-Api-Key': '2jWCY0dASiPZc7RLybXvXA==R9oC0XPKPWiGJ6k6'})
        if response.status_code == requests.codes.ok:
            st.write(f"<h2 style=font-size:29px;color:#9CDBA6;>{response.json()[0]['fact']}</h2>",unsafe_allow_html=True)
    except:
        st.error("Network Error")
