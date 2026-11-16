# Mejorador de Redaccion y Estilo

Este es un proyecto de Asistente de escritura impulsado por Inteligencia Artificial para la clase LLM de Inteligencia Artificial.

## Funcionalidad

La aplicacion esta enfocada en optimizar cualquier texto escritro por el usuario mediante la inteligencia artificial utilizando **Streamlit** para la interfaz grafica y la **API de OpenAI**


- **Corrección y mejora de estilo**: Permite pegar un texto existente para que el modelo corrija errores de ortografía, gramática y puntuación, mejorando su claridad y fluidez sin alterar su significado original.

## 🛠 Requisitos Previos

Para utilizar esta aplicación necesitas:

- Python 3.8 o superior instalado en tu sistema.
- Una **API Key de OpenAI** (Puedes obtenerla en [OpenAI Platform](https://platform.openai.com/)).


## Instalacion

1.- Clona el repositorio o navega hasta la carpeta del proyecto en tu terminal:
    cd /ruta/a/tu/proyecto/asistente_escritura

2.- Se recomienda que crees un entorno virtual para instalar las dependencias sin afectar tu sistema:
    python -m venv venv
     source venv/bin/activate  # En Mac/Linux
     # venv\Scripts\activate   # En Windows

3.- Instala las dependencias requeridas que estan en el archivo 'requeriments.txt':
    pip install -r requirements.txt

Para iniciar la aplicacion asegurate de tener tu entorno virtual activado y ejecuta el comando:
    streamlit run main.py




