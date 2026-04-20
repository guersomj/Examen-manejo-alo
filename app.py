import streamlit as st
import random

st.set_page_config(page_title="Examen de Manejo Alo", page_icon="🚗")

preguntas = [
    {
        "pregunta": "¿Cómo se define a un automovilista?",
        "opciones": [
            "El conductor de cualquier vehículo motorizado",
            "El conductor de vehículo destinado para uso particular",
            "El conductor de transporte público",
            "El propietario del vehículo",
        ],
        "correcta": "El conductor de vehículo destinado para uso particular",
    },
    {
        "pregunta": "¿Quién es considerado chofer según la guía?",
        "opciones": [
            "Todo conductor con licencia vigente",
            "El conductor de motocicleta",
            "El conductor de vehículo destinado al servicio público o particular de pasajeros o carga mediante retribución económica",
            "El acompañante del conductor",
        ],
        "correcta": "El conductor de vehículo destinado al servicio público o particular de pasajeros o carga mediante retribución económica",
    },
    {
        "pregunta": "¿Quién tiene preferencia de paso en todas las intersecciones con señalamiento?",
        "opciones": [
            "Los motociclistas",
            "Los automovilistas",
            "Los peatones",
            "Los choferes",
        ],
        "correcta": "Los peatones",
    },
    {
        "pregunta": "¿Cuál es un requisito para que un vehículo circule en el Estado?",
        "opciones": [
            "Tener sólo combustible suficiente",
            "Portar elementos de identificación vehicular vigentes y coincidentes",
            "Tener polarizado oscuro",
            "Portar sólo licencia vencida",
        ],
        "correcta": "Portar elementos de identificación vehicular vigentes y coincidentes",
    },
    {
        "pregunta": "¿Para quiénes son obligatorios los cinturones de seguridad?",
        "opciones": [
            "Sólo para el conductor",
            "Sólo para pasajeros delanteros",
            "Para el conductor y cada pasajero",
            "Sólo en carretera",
        ],
        "correcta": "Para el conductor y cada pasajero",
    },
    {
        "pregunta": "¿Qué debe hacer un conductor al llegar a una zona peatonal?",
        "opciones": [
            "Acelerar para pasar primero",
            "Detener la marcha para ceder el paso a peatones",
            "Tocar el claxon",
            "Pasar sólo si no hay semáforo",
        ],
        "correcta": "Detener la marcha para ceder el paso a peatones",
    },
    {
        "pregunta": "¿Qué velocidad máxima indica la guía para Tijuana en la ciudad?",
        "opciones": [
            "65 km/h",
            "60 km/h",
            "40 km/h",
            "50 km/h",
        ],
        "correcta": "40 km/h",
    },
    {
        "pregunta": "¿Qué color tiene la señal de ALTO?",
        "opciones": [
            "Fondo blanco con letras negras",
            "Fondo rojo con letras blancas",
            "Fondo azul con letras blancas",
            "Fondo negro con letras rojas",
        ],
        "correcta": "Fondo rojo con letras blancas",
    },
    {
        "pregunta": "¿Qué color de fondo tienen las señales preventivas?",
        "opciones": [
            "Verde",
            "Rojo",
            "Amarillo",
            "Azul",
        ],
        "correcta": "Amarillo",
    },
    {
        "pregunta": "¿Cuál es la distancia mínima lateral que debe respetar un vehículo motorizado respecto al ciclista?",
        "opciones": [
            "50 cm",
            "1 metro",
            "1.50 metros",
            "2 metros",
        ],
        "correcta": "1.50 metros",
    },
]

if "preguntas_actuales" not in st.session_state:
    st.session_state.preguntas_actuales = random.sample(preguntas, 10)

st.title("🚗 Examen de Manejo Alo")
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
