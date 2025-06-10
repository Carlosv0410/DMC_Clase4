import streamlit as st

st.title("Mi primera Aplicación")
st.sidebar.title("Parámetros")

def interes_simple(capital, tasa, tiempo):
    """Calcula el interés simple."""
    return capital * tasa * tiempo
c = st.sidebar.number_input("Ingrese Capital Inicial")
t = st.sidebar.number_input("Ingrese tasa")
ti = st.sidebar.number_input("Ingrese tiempo")
interes = interes_simple(c,t, ti)
st.write(interes)