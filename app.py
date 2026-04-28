import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. ESTILOS CSS (RÉPLICA TOTAL + SOLUCIÓN LOGO + RESPONSIVE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    :root {
        --brand: #2B5AC4;
        --accent: #00B7FF;
    }

    /* Fondo Global y Fuente */
    .stApp {
        background-color: var(--brand) !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    /* OCULTAR HEADER NATIVO */
    header[data-testid="stHeader"] {
        background-color: rgba(43, 90, 196, 0.95) !important;
        backdrop-filter: blur(10px);
    }

    /* ENCABEZADO FIJO COMPACTO */
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 9999;
        background-color: var(--brand);
        padding: 10px 5%;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        display: flex;
        align-items: center;
        gap: 15px;
        height: 80px;
    }

    .logo-img {
        height: 60px;
        width: auto;
        object-fit: contain;
    }

    .header-text h1 {
        margin: 0 !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        color: white !important;
    }

    .header-text p {
        margin: 0 !important;
        color: var(--accent) !important;
        font-weight: 700;
        font-size: 11px;
        text-transform: uppercase;
    }

    /* CONTENEDOR PRINCIPAL (Navegación hacia abajo) */
    .main-scroll-container {
        margin-top: 100px;
        padding: 0 5%;
    }

    .section {
        padding: 60px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .hero-text {
        font-size: clamp(30px, 5vw, 50px);
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 25px;
    }

    /* TARJETAS ESTILO NETLIFY */
    .card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 15px;
        padding: 30px;
        height: 100%;
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        border-color: var(--accent);
    }

    /* OCULTAR MENÚ EN MÓVIL (Sidebar de Streamlit se encarga) */
    @media (max-width: 768px) {
        .nav-desktop { display: none; }
    }

    /* Botones de Formulario */
    .stButton>button {
        background-color: var(--accent) !important;
        color: var(--brand) !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# 3. COMPONENTE ENCABEZADO FIJO (Solución de Logo)
# Usamos una URL de respaldo del escudo oficial para asegurar que siempre se vea
logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png"

st.markdown(f"""
    <div class="fixed-header">
        <img src="{logo_url}" class="logo-img">
        <div class="header-text">
            <h1>Dirección de Servicios Públicos</h1>
            <p>Alcaldía de Villavicencio</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. MENÚ LATERAL (Para Navegador y App Celular)
# En celular se oculta y aparece al desplazar el borde izquierdo o tocar la flecha
with st.sidebar:
    st.markdown("### Navegación")
    st.markdown("---")
    st.markdown("[🏠 Inicio](#inicio)")
    st.markdown("[🏢 Empresas Prestadoras](#empresas)")
    st.markdown("[🙋 Solicitar Orientación](#orientacion)")
    st.markdown("[🔍 ¿Qué hacemos?](#que-hacemos)")
    st.markdown("[📰 Noticias](#noticias)")
    st.markdown("[📞 Contacto](#contacto)")

# 5. CONTENIDO VERTICAL (Navegación toda hacia abajo)
st.markdown('<div class="main-scroll-container">', unsafe_allow_html=True)

# SECCIÓN 1: INICIO / HERO
st.markdown('<div id="inicio" class="section">', unsafe_allow_html=True)
st.markdown('<h1 class="hero-text">Somos el puente entre la ciudadanía y los prestadores de servicios públicos domiciliarios</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px; opacity: 0.9; max-width: 800px;">Te orientamos sobre tus derechos y deberes, rutas de atención y somos el apoyo institucional para mejorar la calidad de vida en Villavicencio.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# SECCIÓN 2: EMPRESAS PRESTADORAS
st.markdown('<div id="empresas" class="section">', unsafe_allow_html=True)
st.title("Empresas Prestadoras")
c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown('<div class="card"><h3>EAAV</h3><p>Acueducto y Alcantarillado</p></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="card"><h3>EMSA</h3><p>Energía Eléctrica</p></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="card"><h3>Llanogas</h3><p>Gas Domiciliario</p></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="card"><h3>Bioagrícola</h3><p>Aseo y Limpieza</p></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# SECCIÓN 3: ORIENTACIÓN CIUDADANA (Formulario)
st.markdown('<div id="orientacion" class="section">', unsafe_allow_html=True)
st.title("Solicitar Orientación")
with st.form("pqr_vertical"):
    st.text_input("Nombre Completo")
    st.selectbox("Servicio", ["Agua", "Luz", "Gas", "Aseo"])
    st.text_area("Describa su inquietud o reclamo")
    st.form_submit_button("Enviar Solicitud")
st.markdown('</div>', unsafe_allow_html=True)

# SECCIÓN 4: ¿QUÉ HACEMOS?
st.markdown('<div id="que-hacemos" class="section">', unsafe_allow_html=True)
st.title("¿Qué hacemos?")
st.markdown("""
    <div class="card">
        <p style="font-size: 18px;">Trabajamos para garantizar que las empresas prestadoras cumplan con los estándares de calidad. 
        Servimos como apoyo técnico a la Alcaldía y como guía jurídica para el ciudadano.</p>
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# SECCIÓN 5: CONTACTO
st.markdown('<div id="contacto" class="section">', unsafe_allow_html=True)
st.title("Contacto")
col_cont1, col_cont2 = st.columns(2)
with col_cont1:
    st.write("📍 Calle 40 No. 33-64 Centro, Edificio Alcaldía")
with col_cont2:
    st.write("📧 serviciospublicos@villavicencio.gov.co")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Cierre contenedor

# 6. FOOTER
st.markdown("""
    <div style="text-align: center; padding: 40px; opacity: 0.5; font-size: 13px; border-top: 1px solid rgba(255,255,255,0.1);">
        © 2026 Alcaldía de Villavicencio — Dirección de Servicios Públicos Domiciliarios
    </div>
""", unsafe_allow_html=True)
