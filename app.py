import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. ESTILOS CSS (Logo lateral + Menú elevado + Header Fijo)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    :root {
        --brand: #2B5AC4;
        --accent: #00B7FF;
    }

    .stApp {
        background-color: var(--brand) !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    /* Ocultar barra superior de Streamlit */
    header[data-testid="stHeader"], [data-testid="stToolbar"] {
        display: none !important;
    }

    /* --- ENCABEZADO FIJO COMPACTO --- */
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        background-color: var(--brand);
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        padding: 12px 5%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .header-layout {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 10px;
    }

    .header-logo {
        height: 50px;
    }

    .header-text h1 {
        margin: 0 !important;
        font-size: 20px !important;
        font-weight: 800 !important;
        line-height: 1 !important;
        color: white !important;
    }

    .header-text p {
        margin: 0 !important;
        color: var(--accent) !important;
        font-weight: 700;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* --- AJUSTE DE POSICIÓN DEL MENÚ --- */
    .main-container {
        margin-top: 155px; /* Ajuste para que el texto inicie justo debajo del header */
    }

    /* Estilo de Pestañas (Tabs) */
    div[data-baseweb="tab-list"] {
        gap: 10px !important;
        background-color: transparent !important;
    }

    /* Pestañas Inactivas */
    div[data-baseweb="tab"] {
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        background-color: transparent !important;
        border-radius: 6px !important;
        padding: 6px 14px !important;
        color: white !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }

    /* Pestaña Activa */
    div[aria-selected="true"] {
        background-color: white !important;
        color: var(--brand) !important;
        border: 1px solid white !important;
    }

    div[data-baseweb="tab-highlight"] { display: none !important; }

    /* Tarjetas de contenido */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. RENDER DEL ENCABEZADO (Logo al lado del Título)
st.markdown("""
    <div class="fixed-header">
        <div class="header-layout">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png" class="header-logo">
            <div class="header-text">
                <h1>Dirección de Servicios Públicos Domiciliarios</h1>
                <p>Alcaldía de Villavicencio</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. CONTENIDO CON MENÚ ELEVADO
st.markdown('<div class="main-container">', unsafe_allow_html=True)

menu = [
    "Inicio", 
    "¿Qué hacemos?", 
    "Empresas prestadoras", 
    "Orientación ciudadana", 
    "Documentos", 
    "Noticias", 
    "Contacto"
]
tabs = st.tabs(menu)

with tabs[0]: # Inicio
    st.markdown("""
        <h2 style="font-size: 40px; line-height: 1.1; margin-bottom: 20px; font-weight: 800;">
            Somos el puente entre la ciudadanía y los prestadores
        </h2>
        <p style="font-size: 18px; color: rgba(255,255,255,0.9); max-width: 850px; line-height: 1.5;">
            Te orientamos sobre tus derechos y deberes, rutas de atención y somos el apoyo institucional para mejorar la calidad de los servicios en Villavicencio.
        </p>
    """, unsafe_allow_html=True)

with tabs[1]: # ¿Qué hacemos?
    st.markdown("### Nuestra Labor")
    st.markdown('<div class="glass-card">Orientamos al ciudadano y vigilamos la calidad de los servicios de agua, energía, gas y aseo.</div>', unsafe_allow_html=True)

with tabs[2]: # Empresas
    st.markdown("### Empresas Prestadoras")
    col1, col2, col3, col4 = st.columns(4)
    col1.button("EAAV")
    col2.button("EMSA")
    col3.button("Llanogas")
    col4.button("Bioagrícola")

with tabs[3]: # Orientación
    st.markdown("### Orientación Ciudadana")
    with st.form("pqr_form"):
        st.text_input("Nombre completo")
        st.text_area("Consulta o requerimiento")
        st.form_submit_button("Enviar consulta")

with tabs[4]: # Documentos
    st.markdown("### Documentos oficiales")
    st.markdown('<div class="glass-card">📂 Guía de usuario - PQR</div>', unsafe_allow_html=True)

with tabs[5]: # Noticias
    st.markdown("### Noticias y Comunicados")
    st.markdown('<div class="glass-card">🔔 Próximas jornadas de atención presencial en barrios.</div>', unsafe_allow_html=True)

with tabs[6]: # Contacto
    st.markdown("### Información de Contacto")
    st.write("📍 Calle 40 No. 33-64 Centro | Villavicencio, Meta")

st.markdown('</div>', unsafe_allow_html=True)

# 5. PIE DE PÁGINA
st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; opacity: 0.5; font-size: 12px; border-top: 1px solid rgba(255,255,255,0.1);">
        Villavicencio, Meta — 2026 | Dirección de Servicios Públicos Domiciliarios
    </div>
""", unsafe_allow_html=True)
