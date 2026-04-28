import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. CSS FINAL (Sin errores de posicionamiento)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    .stApp {
        background-color: #2B5AC4 !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    /* Ocultar barra superior nativa */
    header {display: none !important;}
    
    /* Contenedor del Encabezado */
    .header-container {
        display: flex;
        align-items: center;
        padding: 10px 0;
        margin-bottom: 20px;
    }

    .header-text {
        margin-left: 20px;
    }

    .inst-title {
        font-weight: 800;
        font-size: 22px;
        line-height: 1.1;
        margin: 0;
    }

    .inst-sub {
        color: #00B7FF;
        font-weight: 700;
        font-size: 14px;
        text-transform: uppercase;
        margin-top: 4px;
    }

    /* Hero */
    .hero-title {
        font-size: clamp(30px, 5vw, 52px);
        font-weight: 800;
        line-height: 1.1;
        margin-top: 10px;
    }
    .aguamarina { color: #7FFFD4; }

    /* Botones blancos */
    div.stButton > button {
        background-color: white !important;
        color: #2B5AC4 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        border: none !important;
        width: 100%;
        height: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO (Solución de Logo)
# Usamos columnas pero con un truco para que el logo no falle
col_logo, col_titulo = st.columns([1, 8])

with col_logo:
    # URL directa del escudo. Si no carga, Streamlit mostrará el espacio vacío sin errores.
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png", width=80)

with col_titulo:
    st.markdown("""
        <div class="header-text">
            <p class="inst-title">Dirección de Servicios Públicos Domiciliarios</p>
            <p class="inst-sub">Alcaldía de Villavicencio</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<hr style="border: 0.5px solid rgba(255,255,255,0.2)">', unsafe_allow_html=True)

# 4. CUERPO
st.markdown(f"""
    <h1 class="hero-title">
        Somos el <span class="aguamarina">puente</span> entre la ciudadanía y los prestadores de servicios públicos domiciliarios
    </h1>
    <p style="font-size: 19px; opacity: 0.9; margin-bottom: 30px;">
        Te orientamos sobre tus derechos y deberes, rutas de atención y trámites ante las empresas de acueducto, energía, gas y aseo.
    </p>
""", unsafe_allow_html=True)

# Botones ajustados
c1, c2, c3 = st.columns([2, 2, 3])
with c1:
    st.button("Ver empresas prestadoras")
with c2:
    st.button("Solicitar orientación")
