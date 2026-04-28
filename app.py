import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Dirección de Servicios Públicos Domiciliarios – Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. ESTILOS CSS - RÉPLICA EXACTA
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

    /* OCULTAR ELEMENTOS POR DEFECTO */
    header[data-testid="stHeader"], [data-testid="stToolbar"] {
        display: none !important;
    }

    /* --- ENCABEZADO FIJO --- */
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        background-color: var(--brand);
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        padding: 15px 5%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .header-content {
        display: flex;
        align-items: center;
        gap: 20px;
    }

    .header-text h1 {
        margin: 0;
        font-size: 24px !important;
        font-weight: 800 !important;
        line-height: 1.1;
    }

    .header-text p {
        margin: 0;
        color: var(--accent) !important;
        font-weight: 700;
        font-size: 15px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    /* MARGEN PARA EL CONTENIDO */
    .main-container {
        margin-top: 140px;
    }

    /* --- ESTILO DE MENÚ (TABS) --- */
    div[data-baseweb="tab-list"] {
        gap: 12px !important;
        background-color: transparent !important;
        margin-bottom: 30px !important;
    }

    /* Pestañas NO seleccionadas (Borde blanco) */
    div[data-baseweb="tab"] {
        border: 1px solid rgba(255, 255, 255, 0.8) !important;
        background-color: transparent !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        color: white !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }

    /* Pestaña SELECCIONADA (Fondo blanco, texto azul) */
    div[aria-selected="true"] {
        background-color: white !important;
        color: var(--brand) !important;
        border: 1px solid white !important;
    }

    div[data-baseweb="tab-highlight"] { display: none !important; }

    /* TARJETAS */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
    }

    h2, h3 { color: white !important; font-weight: 800 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. RENDERIZADO DEL ENCABEZADO FIJO
st.markdown("""
    <div class="fixed-header">
        <div class="header-content">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png" width="85">
            <div class="header-text">
                <h1>Dirección de Servicios Públicos Domiciliarios</h1>
                <p>Alcaldía de Villavicencio</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. CONTENIDO PRINCIPAL
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# MENÚ DE NAVEGACIÓN EXACTO
menu_options = [
    "Inicio", 
    "¿Qué hacemos?", 
    "Empresas prestadoras", 
    "Orientación ciudadana", 
    "Documentos", 
    "Noticias y comunicados", 
    "Contacto"
]
tabs = st.tabs(menu_options)

with tabs[0]: # Inicio
    st.markdown("""
        <div style="padding: 20px 0;">
            <h2 style="font-size: 45px; line-height: 1.1; margin-bottom: 20px;">
                Somos el puente entre la ciudadanía y los prestadores de servicios públicos domiciliarios
            </h2>
            <p style="font-size: 19px; color: rgba(255,255,255,0.9); max-width: 900px; line-height: 1.5;">
                Te orientamos sobre tus derechos y deberes, rutas de atención y somos el apoyo institucional para mejorar la calidad de los servicios en Villavicencio.
            </p>
        </div>
    """, unsafe_allow_html=True)

with tabs[1]: # ¿Qué hacemos?
    st.markdown("## ¿Qué hacemos?")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="glass-card"><h3>Orientación</h3><p>Ayudamos al ciudadano a entender su factura y derechos.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="glass-card"><h3>Seguimiento</h3><p>Vigilamos que las empresas cumplan con los indicadores de calidad.</p></div>', unsafe_allow_html=True)

with tabs[2]: # Empresas prestadoras
    st.markdown("## Empresas prestadoras")
    st.write("Canales oficiales de atención:")
    empresas = ["EAAV (Agua)", "EMSA (Energía)", "Llanogas (Gas)", "Bioagrícola (Aseo)"]
    for emp in empresas:
        st.markdown(f'<div class="glass-card"><h3>{emp}</h3><p>Acceso a trámites y reportes.</p></div>', unsafe_allow_html=True)

with tabs[3]: # Orientación ciudadana
    st.markdown("## Orientación ciudadana")
    with st.form("orientacion_form"):
        st.text_input("Nombre completo")
        st.selectbox("Servicio", ["Acueducto", "Energía", "Gas", "Aseo"])
        st.text_area("Descripción de su consulta")
        st.form_submit_button("Enviar Solicitud")

with tabs[4]: # Documentos
    st.markdown("## Documentos")
    st.markdown('<div class="glass-card"><h3>📄 Formato PQR</h3><p>Descargue el modelo para sus reclamaciones.</p></div>', unsafe_allow_html=True)

with tabs[5]: # Noticias y comunicados
    st.markdown("## Noticias y comunicados")
    st.markdown("""
        <div class="glass-card">
            <span style="color:#00B7FF; font-weight:700;">AVISO</span>
            <h3>Jornadas de atención</h3>
            <p>Próximas visitas a las comunas para revisión de facturación.</p>
        </div>
    """, unsafe_allow_html=True)

with tabs[6]: # Contacto
    st.markdown("## Contacto")
    st.info("📍 Calle 40 No. 33-64 Centro | Villavicencio, Meta")

st.markdown('</div>', unsafe_allow_html=True)

# 5. FOOTER
st.markdown("""
    <div style="text-align: center; margin-top: 60px; padding: 30px; border-top: 1px solid rgba(255,255,255,0.1); color: rgba(255,255,255,0.5);">
        © 2026 Alcaldía de Villavicencio — Dirección de Servicios Públicos Domiciliarios.
    </div>
""", unsafe_allow_html=True)
