import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. CSS DE PRECISIÓN
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

    header[data-testid="stHeader"] { display: none !important; }

    /* --- ENCABEZADO FIJO (Logo y Título) --- */
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 10000;
        background-color: var(--brand);
        padding: 10px 5%;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        display: flex;
        align-items: center;
        height: 90px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }

    .header-content {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .logo-img {
        height: 60px;
        width: auto;
    }

    .header-text h1 {
        margin: 0 !important;
        font-size: 20px !important;
        font-weight: 800 !important;
        color: white !important;
        line-height: 1.1 !important;
    }

    .header-text p {
        margin: 0 !important;
        color: var(--accent) !important;
        font-weight: 700;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* --- AJUSTE DE ESPACIO PARA EL CONTENIDO --- */
    .main-scroll-container {
        margin-top: 100px; /* Reducido para eliminar el espacio excesivo */
        padding: 0 5%;
    }

    .section {
        padding: 40px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .hero-text {
        font-size: clamp(30px, 5vw, 55px);
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 25px;
    }

    /* Resaltado Aguamarina */
    .highlight-bridge {
        color: var(--aguamarina);
    }

    .card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 25px;
    }

    /* Sidebar / Menú móvil */
    [data-testid="stSidebar"] { background-color: #1e3d85 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. RENDER DEL ENCABEZADO FIJO (Logo + Títulos)
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

# 4. MENÚ LATERAL (Sidebar)
with st.sidebar:
    st.markdown("### Menú")
    st.markdown("---")
    st.markdown("[🏠 Inicio](#inicio)")
    st.markdown("[🏢 Empresas](#empresas)")
    st.markdown("[🙋 Orientación](#orientacion)")
    st.markdown("[🔍 ¿Qué hacemos?](#que-hacemos)")
    st.markdown("[📞 Contacto](#contacto)")

# 5. CONTENIDO PRINCIPAL
st.markdown('<div class="main-scroll-container">', unsafe_allow_html=True)

# SECCIÓN 1: HERO (Con el color aguamarina en "puente")
st.markdown('<div id="inicio" class="section">', unsafe_allow_html=True)
st.markdown(f"""
    <h1 class="hero-text">
        Somos el <span class="highlight-bridge">puente</span> entre la ciudadanía y los prestadores de servicios públicos domiciliarios
    </h1>
    <p style="font-size: 19px; opacity: 0.9; max-width: 850px;">
        Te orientamos sobre tus derechos y deberes, rutas de atención y somos el apoyo institucional para mejorar la calidad en Villavicencio.
    </p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# SECCIÓN 2: EMPRESAS
st.markdown('<div id="empresas" class="section">', unsafe_allow_html=True)
st.subheader("Empresas Prestadoras")
c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown('<div class="card"><b>EAAV</b><br>Acueducto</div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="card"><b>EMSA</b><br>Energía</div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="card"><b>Llanogas</b><br>Gas</div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="card"><b>Bioagrícola</b><br>Aseo</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# SECCIÓN 3: ORIENTACIÓN
st.markdown('<div id="orientacion" class="section">', unsafe_allow_html=True)
st.subheader("Solicitar Orientación Ciudadana")
with st.form("pqr_main"):
    st.text_input("Nombre completo")
    st.selectbox("Servicio", ["Agua", "Luz", "Gas", "Aseo"])
    st.text_area("Describa su inquietud")
    st.form_submit_button("Enviar")
st.markdown('</div>', unsafe_allow_html=True)

# SECCIÓN 4: ¿QUÉ HACEMOS?
st.markdown('<div id="que-hacemos" class="section">', unsafe_allow_html=True)
st.subheader("¿Qué hacemos?")
st.markdown('<div class="card">Garantizamos que la prestación de los servicios cumpla con los estándares de ley y acompañamos al usuario en sus trámites.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Fin main-scroll-container

# 6. FOOTER
st.markdown("""
    <div style="text-align: center; padding: 30px; opacity: 0.5; font-size: 12px; border-top: 1px solid rgba(255,255,255,0.1);">
        Villavicencio, Meta — 2026
    </div>
""", unsafe_allow_html=True)
