import streamlit as st
import os
from openai import OpenAI

# Configuración básica de la página
st.set_page_config(page_title="Asistente de Escritura", page_icon="✍️", layout="centered") 

st.title("✍️ Asistente de Escritura Automática")
st.write("¡Hola! Soy tu asistente de escritura. Puedo ayudarte a sugerir oraciones, corregir tu gramática, mejorar tu estilo o incluso redactar textos completos.")

api_key_env = os.getenv("OPENAI_API_KEY", "")
api_key = st.text_input(
    "Ingresa tu OpenAI API Key para empezar:",
    value=api_key_env,
    type="password"
)

if api_key:
    client = OpenAI(api_key=api_key)

    texto_usuario = st.text_area("Escribe o pega aquí tu texto:", height=200)

    if st.button("Mejorar redacción"):
            if texto_usuario.strip():
                with st.spinner("Analizando y mejorando tu texto..."):
                    try:
                        response = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[
                                {
                                    "role": "system",
                                    "content": (
                                        "Corrige la ortografía y mejora la redacción y estilo del siguiente texto. Devuelve solo el texto corregido"
                                    )
                                },
                                {
                                    "role": "user",
                                    "content": texto_usuario
                                }
                            ],
                            temperature=0.3
                        )
                        
                        texto_mejorado = response.choices[0].message.content
                        st.subheader("Texto Mejorado:")
                        st.write(texto_mejorado)
                        
                    except Exception as e:
                        st.error(f"Error al conectar con OpenAI: {e}")
            else:
                st.warning("Por favor, ingresa un texto antes de continuar.")
    else:
        st.info("Ingresa tu API Key de OpenAI para comenzar.")
