import streamlit as st

# 1. Configuración de página con icono oficial
st.set_page_config(
    page_title="DSPD Villavicencio", 
    layout="wide", 
    page_icon="https://www.villavicencio.gov.co/favicon.ico"
)

# 2. Estilo CSS Profesional (Mejorado)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .stApp {
        background: linear-gradient(135deg, #1e45a5 0%, #2b59c3 100%);
        color: white;
    }

    /* Navbar Estilizada */
    .nav-link {
        color: rgba(255,255,255,0.8);
        text-decoration: none;
        font-weight: 500;
        font-size: 14px;
        transition: 0.3s;
    }
    .nav-link:hover { color: #4cc9f0; }

    /* Tarjetas de Empresas (Basado en tu imagen image_0de49c) */
    .company-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        color: #1e45a5;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Botones Card (Derecha) */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        border-radius: 20px !important;
        height: 150px !important;
        transition: all 0.4s ease !important;
    }
    div.stButton > button:hover {
        background: rgba(255, 255, 255, 0.15) !important;
        transform: translateY(-8px);
        border: 1px solid #4cc9f0 !important;
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE NAVEGACIÓN ---
if 'page' not in st.session_state:
    st.session_state.page = 'Inicio'

def set_page(name):
    st.session_state.page = name

# --- HEADER / NAVBAR ---
col_logo, col_menu = st.columns([1, 2])
with col_logo:
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 12px; cursor: pointer;">
            <img src="https://www.villavicencio.gov.co/Transparencia/Documents/Logos%20Alcaldia/Escudo%20Alcaldia%20PNG.png" width="55">
            <div style="line-height: 1.1;">
                <div style="font-weight: 800; font-size: 16px;">DSPD Villavicencio</div>
                <div style="font-size: 11px; opacity: 0.7;">Alcaldía de Villavicencio</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_menu:
    cols = st.columns(6)
    if cols[0].button("¿Qué hacemos?", key="m1"): set_page('Inicio')
    if cols[1].button("Empresas", key="m2"): set_page('Empresas')
    if cols[2].button("Orientación", key="m3"): set_page('Orientacion')
    if cols[3].button("Documentos", key="m4"): set_page('Documentos')
    if cols[4].button("Noticias", key="m5"): set_page('Noticias')
    if cols[5].button("Contacto", key="m6"): set_page('Contacto')

# --- LÓGICA DE PÁGINAS ---

if st.session_state.page == 'Inicio':
    col_left, col_right = st.columns([1.2, 1], gap="large")
    with col_left:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
            <h1 style='font-size: 52px; font-weight: 800; line-height: 1;'>
                Somos el <span style='color: #4cc9f0;'>puente</span> entre la ciudadanía y los prestadores
            </h1>
            <p style='font-size: 18px; opacity: 0.9; margin: 25px 0;'>
                Te orientamos sobre derechos y deberes, rutas de atención y trámites ante las empresas de acueducto, energía, gas y aseo.
            </p>
        """, unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: st.button("Ver empresas prestadoras", on_click=lambda: set_page('Empresas'), use_container_width=True)
        with c2: st.button("Solicitar orientación", on_click=lambda: set_page('Orientacion'), use_container_width=True)

    with col_right:
        st.markdown("<br><br>", unsafe_allow_html=True)
        g1, g2 = st.columns(2)
        with g1:
            st.button("⚖️\n\nDerechos", use_container_width=True)
            st.button("🏢\n\nEmpresas", on_click=lambda: set_page('Empresas'), use_container_width=True)
        with g2:
            st.button("🗺️\n\nRutas de atención", use_container_width=True)
            st.button("ℹ️\n\nOrientación DSP", on_click=lambda: set_page('Orientacion'), use_container_width=True)

elif st.session_state.page == 'Empresas':
    st.markdown("## 🏢 Empresas Prestadoras")
    st.write("Consulta el sitio oficial según el servicio que necesites.")
    
    # Listado de empresas (Basado en image_0de49c)
    empresas = [
        {"n": "EAAV", "d": "Acueducto y Alcantarillado", "l": "https://www.eaav.gov.co"},
        {"n": "EMSA", "d": "Electrificadora del Meta", "l": "https://www.emsa-esp.com.co"},
        {"n": "Llanogas S.A.", "d": "Gas Domiciliario", "l": "https://llanogas.com"},
        {"n": "Bioagrícola", "d": "Servicio de Aseo", "l": "https://www.bioagricoladellano.com.co"}
    ]
    
    for emp in empresas:
        with st.container():
            st.markdown(f"""
                <div class="company-card">
                    <div>
                        <strong>{emp['n']}</strong> — {emp['d']}<br>
                        <small style="color: gray;">Sitio oficial</small>
                    </div>
                    <a href="{emp['l']}" target="_blank" style="text-decoration:none;">
                        <button style="padding: 8px 20px; border-radius: 8px; border: 1px solid #1e45a5; background: transparent; color: #1e45a5; cursor: pointer;">Ir al sitio</button>
                    </a>
                </div>
            """, unsafe_allow_html=True)

elif st.session_state.page == 'Orientacion':
    st.markdown("## 📞 Formulario de Orientación")
    with st.form("orientacion_form"):
        c1, c2 = st.columns(2)
        c1.text_input("Nombre completo *")
        c2.text_input("Correo electrónico *")
        t1, t2 = st.columns(2)
        t1.selectbox("Tema de orientación *", ["Facturación", "Calidad del servicio", "Peticiones/Quejas", "Otros"])
        t2.selectbox("Servicio *", ["Acueducto", "Energía", "Gas", "Aseo"])
        st.text_area("Descripción del caso")
        st.checkbox("Declaro que comprendo que este canal es de orientación.")
        st.form_submit_button("Enviar solicitud")

elif st.session_state.page == 'Noticias':
    st.markdown("## 📰 Noticias y comunicados")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("**Jornada de orientación**\n\nPróximo 15 de mayo en el barrio San Benito.")
    with c2:
        st.warning("**Interrupciones programadas**\n\nMantenimiento preventivo red eléctrica.")
    with c3:
        st.success("**Plazos PQR**\n\nRecuerda los tiempos legales para respuestas.")

# --- PIE DE PÁGINA ---
st.markdown(
