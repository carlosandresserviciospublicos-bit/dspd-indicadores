import streamlit as st
import os

# 1. CONFIGURACIÓN (Oculta el menú de Streamlit para ganar espacio)
st.set_page_config(page_title="DSPD Villavicencio", layout="wide", initial_sidebar_state="collapsed")

# 2. ESTILOS CSS (Réplica exacta de Netlify)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap');
    
    .stApp { background-color: #2B5AC4 !important; color: white !important; font-family: 'Montserrat', sans-serif !important; }
    header {display: none !important;} /* Elimina el header gris de Streamlit */
    
    /* Contenedor del encabezado */
    .header-box { display: flex; align-items: center; gap: 20px; margin-bottom: 10px; }
    .inst-title { font-weight: 800; font-size: 24px; margin: 0; line-height: 1.1; }
    .inst-sub { color: #00B7FF; font-weight: 700; font-size: 15px; text-transform: uppercase; margin-top: 5px; }

    /* Hero y Título */
    .hero-title { font-size: clamp(32px, 5vw, 55px); font-weight: 800; margin-top: 10px !important; line-height: 1.1; }
    .aguamarina { color: #7FFFD4; }

    /* Ajuste del bloque de contenido principal para quitar el hueco */
    .block-container { padding-top: 1.5rem !important; }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO (Logo + Texto)
# Usamos columnas nativas para que el logo no falle nunca
col_logo, col_titulo = st.columns([1, 7])

with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=95) # Aquí aparecerá el nuevo logo
    else:
        st.error("Sube el archivo logo.png a GitHub")

with col_titulo:
    st.markdown('<p class="inst-title">Dirección de Servicios Públicos Domiciliarios</p>', unsafe_allow_html=True)
    st.markdown('<p class="inst-sub">Alcaldía de Villavicencio</p>', unsafe_allow_html=True)

st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.2)'>", unsafe_allow_html=True)

# 4. CUERPO (Puente en Aguamarina)
st.markdown(f'<h1 class="hero-title">Somos el <span class="aguamarina">puente</span> entre la ciudadanía y los prestadores</h1>', unsafe_allow_html=True)
st.write("Te orientamos sobre tus derechos y deberes, rutas de atención y trámites.")
