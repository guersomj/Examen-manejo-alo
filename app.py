import streamlit as st
import random
from preguntas import preguntas

st.set_page_config(page_title="Examen de Manejo Alo", page_icon="🐨")

if "preguntas_actuales" not in st.session_state:
    st.session_state.preguntas_actuales = random.sample(preguntas, 10)

st.title("🚗🐨 Examen de Manejo Alo")

if st.button("🔄 Reiniciar preguntas"):
    st.session_state.preguntas_actuales = random.sample(preguntas, 10)
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
    total = len(st.session_state.preguntas_actuales)

    st.markdown("## Resultado")

    for i, pregunta in enumerate(st.session_state.preguntas_actuales, start=1):
        respuesta_usuario = st.session_state.get(f"pregunta_{i}")
        correcta = pregunta["correcta"]

        if respuesta_usuario == correcta:
            aciertos += 1
            st.success(f"Pregunta {i}: Correcta")
        else:
            st.error(f"Pregunta {i}: Incorrecta")
            st.write(f"**Tu respuesta:** {respuesta_usuario}")
            st.write(f"**Respuesta correcta:** {correcta}")

    st.success(f"Obtuviste {aciertos} de {total} aciertos.")
