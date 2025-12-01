import os
# Esto obliga a TensorFlow a usar el modo compatibilidad con versiones antiguas
os.environ['TF_USE_LEGACY_KERAS'] = '1'

import streamlit as st
from tensorflow import keras  
from PIL import Image, ImageOps  
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Reconocimiento Perros vs Gatos", page_icon="🐾")

st.title("🐶 Detector de Mascotas 🐱")
st.write("Usa la cámara para saber si es un perro o un gato.")


