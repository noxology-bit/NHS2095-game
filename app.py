import streamlit as st

with open("game.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.set_page_config(page_title="The Evolution of Combat", layout="centered")
st.components.v1.html(html_content, height=800, scrolling=True)
