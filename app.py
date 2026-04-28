import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. CSS DE ALTO NIVEL (Solución de Logo, Menú Inteligente y Navegación Vertical)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    :root {
        --brand: #2B5AC4;
        --accent: #00B7FF;
    }

    /* Fondo y Fuente */
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

    /* ENCABEZADO FIJO (Logo + Título en una línea) */
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
        height: 85px;
    }

    .header-content {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .logo-img {
        height: 55px;
        width: auto;
        filter: drop-shadow(0px 2px 4px rgba(0,0,0,0.2));
    }

    .header-text h1 {
        margin: 0 !important;
        font-size: clamp(16px, 4vw, 22px) !important;
        font-weight: 800 !important;
        color: white !important;
        line-height: 1.1 !important;
    }

    .header-text p {
        margin: 0 !important;
        color: var(--accent) !important;
        font-weight: 700;
        font-size: clamp(10px, 2vw, 13px);
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* CONTENEDOR DE NAVEGACIÓN VERTICAL */
    .main-scroll {
        margin-top: 110px;
        padding: 0 5%;
    }

    .section-box {
        padding: 50px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* TEXTO HERO (EL PUENTE) */
    .hero-title {
        font-size: clamp(28px, 6vw, 52px);
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 20px;
    }

    /* TARJETAS ESTILO APP */
    .info-card {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 25px;
        transition: 0.3s ease;
    }
    .info-card:hover {
        background: rgba(255, 255, 255, 0.1);
        border-color: var(--accent);
    }

    /* Estilo del Sidebar (Menú móvil/escritorio) */
    [data-testid="stSidebar"] {
        background-color: #1e3d85 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .sidebar-link {
        color: white !important;
        text-decoration: none !important;
        font-weight: 600;
        display: block;
        padding: 10px 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    /* Ajuste de botones de formulario */
    .stButton>button {
        width: 100%;
        background-color: var(--accent) !important;
        color: var(--brand) !important;
        font-weight: 700 !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO FIJO DEFINITIVO
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

# 4. MENÚ LATERAL (Se oculta en móvil automáticamente)
with st.sidebar:
    st.markdown("### Navegación")
    st.markdown("---")
    st.markdown('<a href="#inicio" class="sidebar-link">🏠 Inicio</a>', unsafe_allow_html=True)
    st.markdown('<a href="#empresas" class="sidebar-link">🏢 Empresas Prestadoras</a>', unsafe_allow_html=True)
    st.markdown('<a href="#orientacion" class="sidebar-link">🙋 Solicitar Orientación</a>', unsafe_allow_html=True)
    st.markdown('<a href="#que-hacemos" class="sidebar-link">🔍 ¿Qué hacemos?</a>', unsafe_allow_html=True)
    st.markdown('<a href="#contacto" class="sidebar-link">📞 Contacto</a>', unsafe_allow_html=True)

# 5. CONTENIDO DE NAVEGACIÓN HACIA ABAJO
st.markdown('<div class="main-scroll">', unsafe_allow_html=True)

# --- INICIO / HERO ---
st.markdown('<div id="inicio" class="section-box">', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">Somos el puente entre la ciudadanía y los prestadores de servicios públicos domiciliarios</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px; opacity: 0.9; max-width: 850px;">Garantizamos la transparencia y calidad en los servicios de agua, energía, gas y aseo para todos los villavicenses.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- EMPRESAS PRESTADORAS ---
st.markdown('<div id="empresas" class="section-box">', unsafe_allow_html=True)
st.subheader("Empresas Prestadoras")
c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown('<div class="info-card"><b>EAAV</b><br>Acueducto</div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="info-card"><b>EMSA</b><br>Energía</div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="info-card"><b>Llanogas</b><br>Gas</div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="info-card"><b>Bioagrícola</b><br>Aseo</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- ORIENTACIÓN CIUDADANA ---
st.markdown('<div id="orientacion" class="section-box">', unsafe_allow_html=True)
st.subheader("Canal de Orientación Ciudadana")
with st.form("pqr_form"):
    st.text_input("Nombre y Apellidos")
    st.selectbox("Empresa sobre la que consulta", ["EAAV", "EMSA", "Llanogas", "Bioagrícola", "Otra"])
    st.text_area("Detalle de su solicitud")
    st.form_submit_button("Enviar Orientación")
st.markdown('</div>', unsafe_allow_html=True)

# --- ¿QUÉ HACEMOS? ---
st.markdown('<div id="que-hacemos" class="section-box">', unsafe_allow_html=True)
st.subheader("¿Qué hacemos?")
st.markdown("""
    <div class="info-card">
        <p>Servimos como organismo técnico y de control para asegurar que los prestadores cumplan sus compromisos. 
        Orientamos al usuario en la radicación de PQRS y realizamos seguimiento a la infraestructura de servicios públicos.</p>
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- CONTACTO ---
st.markdown('<div id="contacto" class="section-box">', unsafe_allow_html=True)
st.subheader("Información de Contacto")
col_f1, col_f2 = st.columns(2)
with col_f1:
    st.write("📍 Calle 40 No. 33-64 Centro")
    st.write("🏢 Edificio Alcaldía de Villavicencio")
with col_f2:
    st.write("📧 serviciospublicos@villavicencio.gov.co")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Cierre main-scroll

# 6. FOOTER
st.markdown("""
    <div style="text-align: center; padding: 40px; opacity: 0.5; font-size: 12px; border-top: 1px solid rgba(255,255,255,0.1);">
        Villavicencio, Meta — 2026 | Dirección de Servicios Públicos
    </div>
""", unsafe_allow_html=True)
