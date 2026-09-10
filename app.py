import streamlit as st


st.set_page_config(
    page_title="Hello Streamlit",
    page_icon="👋",
    layout="centered",
)

st.title("Hello, world!")
st.write("To jest pierwsza aplikacja Streamlit w tym repozytorium.")

name = st.text_input("Jak masz na imie?", placeholder="Wpisz imie")

if name:
    st.success(f"Czesc, {name}! Aplikacja dziala poprawnie.")
else:
    st.info("Wpisz imie, zeby zobaczyc personalizowane powitanie.")
