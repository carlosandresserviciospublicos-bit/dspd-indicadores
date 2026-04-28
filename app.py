import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. CSS DE PRECISIÓN PARA LOGO Y ENCABEZADO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    :root {
        --brand: #2B5AC4;
        --accent: #00B7FF;
        --aguamarina: #7FFFD4;
    }

    .stApp {
        background-color: var(--brand) !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    /* Ocultar header nativo de Streamlit que genera el hueco */
    header[data-testid="stHeader"] {
        display: none !important;
    }

    /* ENCABEZADO FIJO (Logo + Título) */
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 110px; /* Altura suficiente para el logo y texto */
        background-color: var(--brand);
        display: flex;
        align-items: center;
        padding: 0 5%;
        z-index: 10000;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }

    .header-content {
        display: flex;
        align-items: center;
        gap: 20px;
    }

    .logo-img {
        height: 75px !important; /* Tamaño grande y claro */
        width: auto;
    }

    .header-text h1 {
        margin: 0 !important;
        font-size: 22px !important;
        font-weight: 800 !important;
        color: white !important;
        line-height: 1.1 !important;
    }

    .header-text p {
        margin: 5px 0 0 0 !important; /* Espacio para que no esté al borde */
        color: var(--accent) !important;
        font-weight: 700;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* AJUSTE DE ESPACIO PARA QUE EL TEXTO NO SE META DEBAJO DEL HEADER */
    .main-container {
        margin-top: 130px; /* Este margen elimina el espacio excesivo pero evita el solapamiento */
        padding: 0 5%;
    }

    .hero-title {
        font-size: clamp(30px, 5vw, 55px);
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 25px;
    }

    .highlight {
        color: var(--aguamarina);
    }
    </style>
""", unsafe_allow_html=True)

# 3. RENDER DEL ENCABEZADO FIJO
# URL del logo (asegúrate de que esta URL sea accesible)
logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png"

st.markdown(f"""
    <div class="fixed-header">
        <div class="header-content">
            <img src="{logo_url}" class="logo-img">
            <div class="header-text">
                <h1>Dirección de Servicios Públicos Domiciliarios</h1>
                <p>Alcaldía de Villavicencio</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. CONTENIDO PRINCIPAL
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Título Hero
st.markdown(f"""
    <h1 class="hero-title">
        Somos el <span class="highlight">puente</span> entre la ciudadanía y los prestadores de servicios públicos domiciliarios
    </h1>
""", unsafe_allow_html=True)

st.write("Te orientamos sobre tus derechos y deberes, rutas de atención y trámites ante las empresas de acueducto, energía, gas y aseo.")

# Botones de acción
col1, col2 = st.columns([1, 4])
with col1:
    st.button("Ver empresas prestadoras")
with col2:
    st.button("Solicitar orientación")

st.markdown('</div>', unsafe_allow_html=True)
