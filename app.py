import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Dirección de Servicios Públicos Domiciliarios – Alcaldía de Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="https://www.villavicencio.gov.co/favicon.ico"
)

# 2. INYECCIÓN DE ESTILOS (Réplica de Tailwind del .txt)
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

    /* Estilo de Tarjetas del archivo original */
    .custom-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 16px;
    }
    
    .accent-text {
        color: var(--accent) !important;
        font-weight: 700;
        text-transform: uppercase;
        font-size: 13px;
        letter-spacing: 1px;
    }

    h1, h2, h3 { color: white !important; }

    /* Ajuste de pestañas (Tabs) para que parezcan menú de navegación */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(0,0,0,0.1);
        padding: 10px;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: white !important;
        border-radius: 5px;
    }

    .stTabs [aria-selected="true"] {
        background-color: var(--accent) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. CABECERA (LOGO Y TÍTULO)
col_logo, col_titulo = st.columns([1, 6])
with col_logo:
    try:
        st.image("logo.png", width=90)
    except:
        # Fallback en caso de que no encuentre el archivo local
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png", width=85)

with col_titulo:
    st.markdown("""
        <div style="margin-top: 10px;">
            <h1 style="margin: 0; font-size: 24px; font-weight: 800; line-height: 1.1;">
                Dirección de Servicios Públicos Domiciliarios
            </h1>
            <p class="accent-text" style="margin: 0;">Alcaldía de Villavicencio</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border-top: 1px solid rgba(255,255,255,0.1)'>", unsafe_allow_html=True)

# 4. SISTEMA DE NAVEGACIÓN (Secciones del sitio anterior)
tabs = st.tabs(["🏠 Inicio", "❓ ¿Qué hacemos?", "🏢 Empresas", "🙋 Orientación", "📂 Documentos", "📰 Noticias"])

# --- SECCIÓN: INICIO ---
with tabs[0]:
    st.markdown("""
        <div style="padding: 40px 0;">
            <h2 style="font-size: 40px; font-weight: 800; line-height: 1.1; margin-bottom: 20px;">
                Somos el puente entre la ciudadanía y los prestadores de servicios públicos domiciliarios
            </h2>
            <p style="font-size: 18px; color: rgba(255,255,255,0.85); max-width: 850px; line-height: 1.6;">
                Te orientamos sobre tus derechos y deberes, rutas de atención y somos el apoyo institucional 
                para mejorar la calidad de los servicios de agua, energía, gas y aseo en nuestra ciudad.
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.info("📍 Ubicación: Calle 40 No. 33-64 Centro | Horario: 8:00 a.m. – 12:00 m / 2:00 p.m. - 5:00 p.m.")

# --- SECCIÓN: ¿QUÉ HACEMOS? ---
with tabs[1]:
    st.markdown("## ¿Qué hacemos?")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="custom-card">
            <span class="accent-text">Misión</span>
            <h3>Protección al Ciudadano</h3>
            <p>Brindamos las herramientas necesarias para que los usuarios conozcan cómo radicar una PQR y defender sus derechos ante cobros excesivos o fallas técnicas.</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="custom-card">
            <span class="accent-text">Control</span>
            <h3>Mesas Técnicas</h3>
            <p>Articulamos con las empresas prestadoras para supervisar la ejecución de planes de inversión que mejoren la infraestructura de servicios públicos.</p>
        </div>""", unsafe_allow_html=True)

# --- SECCIÓN: EMPRESAS ---
with tabs[2]:
    st.markdown("## Empresas Prestadoras")
    st.write("Acceda directamente a los portales oficiales:")
    
    empresas = [
        ("EAAV", "Acueducto y Alcantarillado", "https://www.eaav.gov.co/"),
        ("EMSA", "Electrificadora del Meta", "https://www.electrificadoradelmeta.com.co/"),
        ("Llanogas", "Gas Domiciliario", "https://www.llanogas.com/"),
        ("Bioagrícola", "Aseo y Limpieza Urbana", "https://www.bioagricoladelllano.com.co/")
    ]
    
    grid = st.columns(2)
    for i, (nombre, desc, link) in enumerate(empresas):
        with grid[i % 2]:
            st.markdown(f"""<div class="custom-card">
                <h3 style="margin-bottom:5px;">{nombre}</h3>
                <p style="font-size:14px;">{desc}</p>
            </div>""", unsafe_allow_html=True)
            st.link_button(f"Ir al sitio de {nombre}", link)

# --- SECCIÓN: ORIENTACIÓN ---
with tabs[3]:
    st.markdown("## Canal de Orientación Ciudadana")
    with st.form("form_orienta"):
        st.write("Complete sus datos para recibir guía técnica:")
        f1, f2 = st.columns(2)
        f1.text_input("Nombre completo")
        f2.text_input("Correo electrónico")
        st.selectbox("Servicio con inconvenientes", ["Agua", "Energía", "Gas", "Aseo"])
        st.text_area("Describa su situación")
        if st.form_submit_button("Enviar Solicitud"):
            st.success("Hemos recibido su solicitud de orientación.")

# --- SECCIÓN: DOCUMENTOS ---
with tabs[4]:
    st.markdown("## Documentos y Normatividad")
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.markdown("""<div class="custom-card">
            <span class="accent-text">Guía</span>
            <h3>Modelo de PQR</h3>
            <p>Descargue el formato estándar para presentar reclamaciones formales.</p>
        </div>""", unsafe_allow_html=True)
        st.button("Descargar PDF")
    with col_d2:
        st.markdown("""<div class="custom-card">
            <span class="accent-text">Legal</span>
            <h3>Ley 142 de 1994</h3>
            <p>Consulte el régimen general de servicios públicos domiciliarios.</p>
        </div>""", unsafe_allow_html=True)
        st.button("Consultar Ley")

# --- SECCIÓN: NOTICIAS ---
with tabs[5]:
    st.markdown("## Noticias y Comunicados")
    st.markdown("""
        <div class="custom-card">
            <span class="accent-text">Aviso · Abril 2026</span>
            <h3>Nuevas jornadas de atención</h3>
            <p>Estaremos en los centros de participación ciudadana brindando asesoría presencial sobre su factura.</p>
        </div>
    """, unsafe_allow_html=True)

# 5. PIE DE PÁGINA
st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 30px; border-top: 1px solid rgba(255,255,255,0.1); color: rgba(255,255,255,0.5); font-size: 13px;">
        © 2026 Alcaldía de Villavicencio — Dirección de Servicios Públicos Domiciliarios.
    </div>
""", unsafe_allow_html=True)
