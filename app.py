import streamlit as st
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. ESTILOS CSS COMPLETOS (Encabezado + Hero + Tarjetas)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    .stApp {
        background-color: #2B5AC4 !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    /* Ocultar elementos nativos */
    header {display: none !important;}
    .block-container {padding-top: 1rem !important;}

    /* Encabezado Institucional */
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

    /* Hero Section */
    .hero-title {
        font-size: clamp(32px, 5vw, 55px);
        font-weight: 800;
        line-height: 1.1;
        margin-top: 15px !important;
    }
    .aguamarina { color: #7FFFD4; }

    /* Botones Principales */
    div.stButton > button {
        background-color: white !important;
        color: #2B5AC4 !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
        border: none !important;
        height: 48px;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #00B7FF !important;
        color: white !important;
    }

    /* SECCIÓN DE TARJETAS (CARDS) */
    .card-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
        margin-top: 50px;
        margin-bottom: 50px;
    }

    .card {
        background-color: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 40px 20px;
        text-align: center;
        transition: all 0.3s ease;
        min-height: 160px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .card:hover {
        background-color: rgba(255, 255, 255, 0.15);
        transform: translateY(-8px);
        border-color: #7FFFD4;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }

    .card-text {
        font-weight: 700;
        font-size: 19px;
        line-height: 1.2;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 3. RENDER DEL ENCABEZADO
col_logo, col_titulo = st.columns([1, 7])

with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=95)
    else:
        st.write("🔄")

with col_titulo:
    st.markdown('<p class="inst-title">Dirección de Servicios Públicos Domiciliarios</p>', unsafe_allow_html=True)
    st.markdown('<p class="inst-sub">Alcaldía de Villavicencio</p>', unsafe_allow_html=True)

st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.15); margin: 15px 0;'>", unsafe_allow_html=True)

# 4. CUERPO PRINCIPAL
st.markdown(f"""
    <h1 class="hero-title">
        Somos el <span class="aguamarina">puente</span> entre la ciudadanía y los prestadores de servicios públicos domiciliarios
    </h1>
    <p style="font-size: 20px; opacity: 0.9; margin-bottom: 25px; max-width: 800px;">
        Te orientamos sobre tus derechos y deberes, rutas de atención y trámites ante las empresas de acueducto, energía, gas y aseo.
    </p>
""", unsafe_allow_html=True)

# Botones de Llamado a la Acción
c1, c2, c3 = st.columns([2.5, 2.5, 5])
with c1:
    st.button("Ver empresas prestadoras")
with c2:
    st.button("Solicitar orientación")

# 5. RENDER DE TARJETAS
st.markdown("""
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

# 6. FOOTER SUTIL
st.markdown("""
    <div style="text-align: center; margin-top: 50px; opacity: 0.5; font-size: 13px;">
        © 2026 Dirección de Servicios Públicos - Villavicencio, Meta
    </div>
""", unsafe_allow_html=True)
