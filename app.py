import streamlit as st
import base64
import requests
from io import BytesIO

# 1. CONFIGURACIÓN
st.set_page_config(page_title="DSPD Villavicencio", layout="wide", initial_sidebar_state="collapsed")

# 2. FUNCIÓN PARA CARGAR LOGO (Solución definitiva)
def get_base64_logo():
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png"
    try:
        response = requests.get(url)
        return base64.b64encode(response.content).decode()
    except:
        return ""

logo_base64 = get_base64_logo()

# 3. CSS DE PRECISIÓN
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    :root {{
        --brand: #2B5AC4;
        --accent: #00B7FF;
        --aguamarina: #7FFFD4;
    }}

    .stApp {{
        background-color: var(--brand) !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
    }}

    /* Ocultar barra superior nativa */
    header[data-testid="stHeader"] {{ display: none !important; }}

    /* ENCABEZADO FIJO */
    .fixed-header {{
        position: fixed;
        top: 0; left: 0; width: 100%;
        height: 100px;
        background-color: var(--brand);
        display: flex;
        align-items: center;
        padding: 0 5%;
        z-index: 10000;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    }}

    .header-content {{
        display: flex;
        align-items: center;
        gap: 15px;
    }}

    /* Imagen forzada en Base64 */
    .logo-container {{
        width: 65px;
        height: 65px;
        background-image: url('data:image/png;base64,{logo_base64}');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
    }}

    .header-text h1 {{
        margin: 0 !important;
        font-size: 20px !important;
        font-weight: 800 !important;
        line-height: 1.1;
    }}

    .header-text p {{
        margin: 5px 0 0 0 !important;
        color: var(--accent) !important;
        font-weight: 700;
        font-size: 13px;
        text-transform: uppercase;
    }}

    /* CONTENIDO (Ajuste de hueco) */
    .main-container {{
        margin-top: 80px; /* Reducido para que no haya hueco grande */
        padding: 20px 5%;
    }}

    .hero-title {{
        font-size: clamp(30px, 5vw, 55px);
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 15px;
    }}

    .highlight {{ color: var(--aguamarina); }}

    /* BOTONES */
    .stButton>button {{
        background-color: white !important;
        color: var(--brand) !important;
        font-weight: 700;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# 4. RENDER HEADER
st.markdown(f"""
    <div class="fixed-header">
        <div class="header-content">
            <div class="logo-container"></div>
            <div class="header-text">
                <h1>Dirección de Servicios Públicos Domiciliarios</h1>
                <p>Alcaldía de Villavicencio</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. RENDER CONTENIDO
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown(f"""
    <h1 class="hero-title">
        Somos el <span class="highlight">puente</span> entre la ciudadanía y los prestadores de servicios públicos domiciliarios
    </h1>
    <p style="font-size: 18px; margin-bottom: 25px;">
        Te orientamos sobre tus derechos y deberes, rutas de atención y trámites ante las empresas de acueducto, energía, gas y aseo.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])
with col1:
    st.button("Ver empresas prestadoras")
with col2:
    st.button("Solicitar orientación")

st.markdown('</div>', unsafe_allow_html=True)
