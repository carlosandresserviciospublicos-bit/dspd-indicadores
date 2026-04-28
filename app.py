import streamlit as st
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. CSS DE PRECISIÓN (Sin huecos y con fuentes correctas)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    .stApp {
        background-color: #2B5AC4 !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    /* OCULTAR ELEMENTOS NATIVOS */
    header {display: none !important;}
    .block-container {padding-top: 1rem !important;}

    /* ENCABEZADO */
    .inst-title {
        font-weight: 800;
        font-size: 24px;
        line-height: 1.1;
        margin: 0 !important;
    }
    .inst-sub {
        color: #00B7FF;
        font-weight: 700;
        font-size: 15px;
        text-transform: uppercase;
        margin-top: 4px !important;
    }

    /* TÍTULO PRINCIPAL (HERO) */
    .hero-title {
        font-size: clamp(32px, 5vw, 55px);
        font-weight: 800;
        line-height: 1.1;
        margin-top: 15px !important;
    }
    .aguamarina { color: #7FFFD4; }

    /* BOTONES */
    div.stButton > button {
        background-color: white !important;
        color: #2B5AC4 !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
        border: none !important;
        height: 48px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# 3. RENDER DEL ENCABEZADO
col_logo, col_titulo = st.columns([1, 7])

with col_logo:
    # Busca el archivo que subiste
    if os.path.exists("logo.png"):
        st.image("logo.png", width=95)
    else:
        st.error("Archivo logo.png no encontrado")

with col_titulo:
    st.markdown('<p class="inst-title">Dirección de Servicios Públicos Domiciliarios</p>', unsafe_allow_html=True)
    st.markdown('<p class="inst-sub">Alcaldía de Villavicencio</p>', unsafe_allow_html=True)

st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.2); margin: 15px 0;'>", unsafe_allow_html=True)

# 4. CUERPO DE LA PÁGINA
st.markdown(f"""
    <h1 class="hero-title">
        Somos el <span class="aguamarina">puente</span> entre la ciudadanía y los prestadores de servicios públicos domiciliarios
    </h1>
    <p style="font-size: 19px; opacity: 0.9; margin-bottom: 25px;">
        Te orientamos sobre tus derechos y deberes, rutas de atención y trámites ante las empresas de acueducto, energía, gas y aseo.
    </p>
""", unsafe_allow_html=True)

# BOTONES
c1, c2, c3 = st.columns([2.5, 2.5, 5])
with c1:
    st.button("Ver empresas prestadoras")
with c2:
    st.button("Solicitar orientación")

# 5. SECCIÓN DE TARJETAS DE SERVICIOS
st.markdown("""
    <style>
    /* Estilo de la cuadrícula de tarjetas */
    .card-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin-top: 40px;
    }

    /* Estilo de cada tarjeta individual */
    .card {
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 30px 20px;
        text-align: center;
        transition: transform 0.3s, background-color 0.3s;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 180px;
    }

    .card:hover {
        background-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-5px);
        border-color: #7FFFD4;
    }

    .card-text {
        font-weight: 600;
        font-size: 18px;
        color: white;
    }
    </style>

    <div class="card-container">
        <div class="card">
            <div class="card-text">Derechos y Deberes</div>
        </div>
        <div class="card">
            <div class="card-text">Rutas de atención</div>
        </div>
        <div class="card">
            <div class="card-text">Empresas Prestadoras</div>
        </div>
        <div class="card">
            <div class="card-text">Orientación DSP</div>
        </div>
    </div>
""", unsafe_allow_html=True)
