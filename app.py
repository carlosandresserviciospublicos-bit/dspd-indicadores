import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. ESTILOS CSS PERSONALIZADOS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    :root {
        --brand: #2B5AC4;
        --accent: #00B7FF;
    }

    /* Fondo general */
    .stApp {
        background-color: var(--brand) !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    /* --- ESTILO DE PESTAÑAS (TABS) --- */
    /* Contenedor de las pestañas */
    div[data-baseweb="tab-list"] {
        gap: 12px !important;
        background-color: transparent !important;
    }

    /* Pestañas NO seleccionadas (Borde blanco, fondo transparente) */
    div[data-baseweb="tab"] {
        border: 1px solid rgba(255, 255, 255, 0.8) !important;
        background-color: transparent !important;
        border-radius: 8px !important;
        padding: 8px 16px !important;
        color: white !important;
        transition: all 0.3s ease !important;
    }

    /* Pestaña SELECCIONADA (Fondo blanco, texto azul) */
    div[aria-selected="true"] {
        background-color: white !important;
        color: var(--brand) !important;
        border: 1px solid white !important;
    }

    /* Hover en pestañas */
    div[data-baseweb="tab"]:hover {
        border-color: var(--accent) !important;
        color: var(--accent) !important;
    }

    /* Quitar la línea inferior roja/azul por defecto de Streamlit */
    div[data-baseweb="tab-highlight"] {
        background-color: transparent !important;
    }

    /* --- TARJETAS Y CONTENIDO --- */
    .card-site {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
    }

    h1, h2, h3 { color: white !important; font-weight: 800 !important; }
    .accent-tag { color: var(--accent); font-weight: 700; text-transform: uppercase; font-size: 13px; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER
col1, col2 = st.columns([1, 6])
with col1:
    try:
        st.image("logo.png", width=95)
    except:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png", width=90)

with col2:
    st.markdown("""
        <div style="margin-top: 5px;">
            <h1 style="margin: 0; font-size: 26px; line-height: 1.1;">Dirección de Servicios Públicos Domiciliarios</h1>
            <p style="color: #00B7FF; margin: 0; font-size: 16px; font-weight: 700; text-transform: uppercase;">Alcaldía de Villavicencio</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border-top: 1px solid rgba(255,255,255,0.2)'>", unsafe_allow_html=True)

# 4. NAVEGACIÓN (Réplica del sistema solicitado)
tabs = st.tabs(["Inicio", "¿Qué hacemos?", "Empresas", "Orientación", "Documentos", "Noticias"])

with tabs[0]:
    st.markdown("""
        <div style="padding: 30px 0;">
            <h2 style="font-size: 42px; line-height: 1.1; margin-bottom: 20px;">
                Somos el puente entre la ciudadanía y los prestadores de servicios públicos
            </h2>
            <p style="font-size: 19px; color: rgba(255,255,255,0.9); max-width: 900px;">
                Te orientamos sobre tus derechos y deberes, rutas de atención y apoyo institucional.
            </p>
        </div>
    """, unsafe_allow_html=True)

with tabs[1]:
    st.markdown("## ¿Qué hacemos?")
    st.markdown("""<div class="card-site">
        <span class="accent-tag">Misión Institucional</span>
        <p>Velar por la correcta prestación de los servicios públicos en el municipio de Villavicencio.</p>
    </div>""", unsafe_allow_html=True)

with tabs[2]:
    st.markdown("## Empresas Prestadoras")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card-site"><h3>EAAV</h3><p>Acueducto y Alcantarillado</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card-site"><h3>EMSA</h3><p>Energía Eléctrica</p></div>', unsafe_allow_html=True)

# ... (Resto de secciones siguen la misma lógica)

# 5. FOOTER
st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid rgba(255,255,255,0.1); color: rgba(255,255,255,0.5);">
        © 2026 Alcaldía de Villavicencio — Dirección de Servicios Públicos Domiciliarios.
    </div>
""", unsafe_allow_html=True)
