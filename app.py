import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA (Base)
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed", # Sidebar cerrado por defecto
)

# 2. ESTILOS CSS - SOLUCIÓN DE FONDO
# Reemplaza todo el bloque CSS anterior por este. Es más limpio y robusto.
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    :root {
        --brand: #2B5AC4;
        --accent: #00B7FF;
        --aguamarina: #7FFFD4;
        --text-white: #FFFFFF;
    }

    /* Fondo Global y Fuente Principal */
    .stApp {
        background-color: var(--brand) !important;
        color: var(--text-white) !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    /* OCULTAR EL HEADER NATIVO DE STREAMLIT (El que causa el hueco) */
    header[data-testid="stHeader"] {
        display: none !important;
    }

    /* --- ENCABEZADO PERSONALIZADO FIJO --- */
    #custom-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 9999; /* Asegura que esté por encima de todo */
        background-color: var(--brand);
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        padding: 10px 5%; /* Padding controlado */
        display: flex;
        align-items: center;
        height: 100px; /* Alto fijo y controlado */
        box-shadow: 0 4px 12px rgba(0,0,0,0.2); /* Sombra para profundidad */
    }

    #header-container {
        display: flex;
        align-items: center;
        gap: 15px; /* Espacio entre logo y texto */
        width: 100%;
    }

    #logo-img {
        height: 65px; /* Tamaño del logo ajustado y visible */
        width: auto;
        border-radius: 50%; /* Opcional: forma circular para el logo */
    }

    #header-text {
        color: var(--text-white) !important;
    }

    #header-text h1 {
        margin: 0 !important;
        font-size: 24px !important;
        font-weight: 800 !important;
        line-height: 1.1 !important;
    }

    #header-text p {
        margin: 0 !important;
        color: var(--accent) !important;
        font-weight: 700;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* --- AJUSTE DE ESPACIO PARA EL CONTENIDO --- */
    /* Este es el cambio clave para eliminar el hueco */
    .main-content {
        margin-top: 110px; /* Exactamente el alto del header + un pequeño margen */
        padding: 0 5%;
    }

    /* --- SISTEMA DE PESTAÑAS COMO MENÚ --- */
    /* Para PC */
    div[data-baseweb="tab-list"] {
        background-color: transparent !important;
        gap: 10px;
        margin-bottom: 30px;
    }
    
    div[data-baseweb="tab"] {
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        background-color: transparent !important;
        border-radius: 5px;
        padding: 8px 16px;
        color: var(--text-white) !important;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    /* Pestaña activa (blanco) */
    div[aria-selected="true"] {
        background-color: var(--text-white) !important;
        color: var(--brand) !important;
    }
    
    /* Hover en pestañas */
    div[data-baseweb="tab"]:hover {
        border-color: var(--accent) !important;
        color: var(--accent) !important;
    }

    /* Ocultar línea roja predeterminada */
    div[data-baseweb="tab-highlight"] {
        background-color: transparent !important;
    }

    /* --- SECCIONES DE CONTENIDO --- */
    .hero-text {
        font-size: clamp(30px, 5vw, 55px);
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 25px;
    }

    /* Palabra "puente" en aguamarina */
    .aguamarina-text {
        color: var(--aguamarina);
    }

    .card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
    }
    
    /* Estilos para formularios y botones */
    .stButton>button {
        background-color: var(--text-white) !important;
        color: var(--brand) !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 8px !important;
    }

    </style>
""", unsafe_allow_html=True)

# 3. RENDER DEL ENCABEZADO FIJO (Contenedor HTML Único)
# Usamos HTML directo para un control total. Asegúrate de tener 'logo.png' o cambia la URL.
logo_fallback_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png"

st.markdown(f"""
    <div id="custom-header">
        <div id="header-container">
            <img src="{logo_fallback_url}" id="logo-img">
            <div id="header-text">
                <h1>Dirección de Servicios Públicos Domiciliarios</h1>
                <p>Alcaldía de Villavicencio</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. CONTENIDO PRINCIPAL (Dentro del div con margen superior)
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Sistema de Pestañas como Menú de Navegación (Toda la navegación hacia abajo)
# menu_options = ["🏠 Inicio", "🏢 Empresas Prestadoras", "🙋 Solicitar Orientación", "🔍 ¿Qué hacemos?"]
# tabs = st.tabs(menu_options)

# Para replicar exactamente el comportamiento de One-Page de Netlify, usaremos botones de ancla.
c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown('<a href="#que-hacemos">¿Qué hacemos?</a>', unsafe_allow_html=True)
with c2: st.markdown('<a href="#empresas">Empresas</a>', unsafe_allow_html=True)
# ... (Los demás enlaces)
st.markdown("---")


# --- SECCIÓN 1: INICIO (Texto del Hero) ---
st.markdown(f"""
    <h1 class="hero-text">
        Somos el <span class="aguamarina-text">puente</span> entre la ciudadanía y los prestadores de servicios públicos domiciliarios
    </h1>
    <p style="font-size: 19px; opacity: 0.9; max-width: 850px; margin-bottom: 30px;">
        Te orientamos sobre tus derechos y deberes, rutas de atención y somos el apoyo institucional para mejorar la calidad en Villavicencio.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.button("Ver empresas prestadoras")
with col2:
    st.button("Solicitar orientación")

st.markdown("---")

# --- SECCIÓN 2: ¿QUÉ HACEMOS? (Con ID para ancla) ---
st.markdown('<div id="que-hacemos"></div>', unsafe_allow_html=True)
st.subheader("¿Qué hacemos?")
st.markdown('<div class="card">Orientamos al ciudadano y vigilamos la calidad de los servicios de agua, energía, gas y aseo.</div>', unsafe_allow_html=True)

# --- SECCIÓN 3: EMPRESAS (Con ID para ancla) ---
st.markdown('<div id="empresas"></div>', unsafe_allow_html=True)
st.subheader("Empresas Prestadoras")
st.write("📍 Calle 40 No. 33-64 Centro")

st.markdown('</div>', unsafe_allow_html=True) # Cierre main-content

# 5. FOOTER
st.markdown("""
    <footer style="text-align: center; padding: 30px; opacity: 0.5; font-size: 12px; border-top: 1px solid rgba(255,255,255,0.1);">
        Villavicencio, Meta — 2026 | Dirección de Servicios Públicos
    </footer>
""", unsafe_allow_html=True)
