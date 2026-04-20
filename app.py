import streamlit as st
import random
from preguntas import preguntas

st.set_page_config(page_title="Examen de Manejo Alo", page_icon="🐨")

if "preguntas_actuales" not in st.session_state:
    st.session_state.preguntas_actuales = random.sample(preguntas, 10)

st.title("🚗🐨 Examen de Manejo Alo")
st.write("Prueba inicial de 10 preguntas.")
st.write("Más adelante meteremos las 100 completas y las escogeremos aleatoriamente.")

if st.button("🔄 Reiniciar preguntas"):
    st.session_state.preguntas_actuales = random.sample(preguntas, len(preguntas))
    st.rerun()

for i, pregunta in enumerate(st.session_state.preguntas_actuales, start=1):
    st.subheader(f"Pregunta {i}")
    respuesta = st.radio(
        pregunta["pregunta"],
        pregunta["opciones"],
        key=f"pregunta_{i}"
    )
if st.button("✅ Calificar examen"):
    aciertos = 0

    for i, pregunta in enumerate(st.session_state.preguntas_actuales, start=1):
        respuesta_usuario = st.session_state.get(f"pregunta_{i}")
        if respuesta_usuario == pregunta["correcta"]:
            aciertos += 1

    st.success(f"Obtuviste {aciertos} de {len(st.session_state.preguntas_actuales)} aciertos.")
