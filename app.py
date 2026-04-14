import streamlit as st
import base64

# 1. Configuración de página (Debe ser lo primero)
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    page_icon="https://www.villavicencio.gov.co/favicon.ico"
)

# --- HEADER / NAVBAR ---
# Usamos columnas nativas para evitar errores de CSS
col1, col2 = st.columns([1, 5])

with col1:
    try:
        # Intenta cargar el logo local que subiste
        st.image("logo.png", width=100)
    except:
        # Si no lo encuentra, usa el link directo para que no salga error
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png", width=100)

with col2:
    # Texto alineado correctamente sin indentaciones extrañas
    st.markdown("""
<div style="margin-top: -5px;">
    <h1 style="color: white; margin-bottom: 0; font-size: 30px; font-family: sans-serif;">
        Dirección de Servicios Públicos Domiciliarios
    </h1>
    <p style="color: #4cc9f0; font-size: 18px; margin-top: 0; font-family: sans-serif;">
        Alcaldía de Villavicencio
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# 2. Estilo CSS Profesional
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .stApp {
        background: linear-gradient(135deg, #1e45a5 0%, #2b59c3 100%);
        color: white;
    }

    /* Tarjetas de Empresas */
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
    
    /* Botones Card del Inicio */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        border-radius: 20px !important;
        height: 150px !important;
        transition: all 0.4s ease !important;
        font-weight: 600 !important;
    }
    div.stButton > button:hover {
        background: rgba(255, 255, 255, 0.15) !important;
        transform: translateY(-8px);
        border: 1px solid #4cc9f0 !important;
    }

    /* Ocultar elementos de Streamlit */
    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE NAVEGACIÓN ---
if 'page' not in st.session_state:
    st.session_state.page = 'Inicio'

def set_page(name):
    st.session_state.page = name

# --- HEADER / NAVBAR ---
# --- HEADER / NAVBAR ---
st.markdown("""
    <div style="display: flex; align-items: center; gap: 18px; margin-bottom: 30px; padding: 10px 0;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Escudo_de_Villavicencio.png" width="75" style="filter: drop-shadow(0px 2px 4px rgba(0,0,0,0.2));">
        <div style="line-height: 1.1; color: white;">
            <div style="font-weight: 800; font-size: 24px; font-family: 'Inter', sans-serif;">Dirección de Servicios Públicos Domiciliarios</div>
            <div style="font-size: 16px; font-weight: 400; opacity: 0.95; font-family: 'Inter', sans-serif;">Alcaldía de Villavicencio</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Menú de navegación superior
cols_menu = st.columns(6)
if cols_menu[0].button("🏠 Inicio", key="nav_ini"): set_page('Inicio')
if cols_menu[1].button("🏢 Empresas", key="nav_emp"): set_page('Empresas')
if cols_menu[2].button("📞 Orientación", key="nav_ori"): set_page('Orientacion')
if cols_menu[3].button("📄 Documentos", key="nav_doc"): set_page('Documentos')
if cols_menu[4].button("📰 Noticias", key="nav_not"): set_page('Noticias')
if cols_menu[5].button("✉️ Contacto", key="nav_con"): set_page('Contacto')

st.markdown("---")

# --- LÓGICA DE PÁGINAS ---

if st.session_state.page == 'Inicio':
    col_left, col_right = st.columns([1.2, 1], gap="large")
    with col_left:
        st.markdown("""
            <h1 style='font-size: 48px; font-weight: 800; line-height: 1.1;'>
                Somos el <span style='color: #4cc9f0;'>puente</span> entre la ciudadanía y los prestadores
            </h1>
            <p style='font-size: 18px; opacity: 0.9; margin: 25px 0;'>
                Te orientamos sobre derechos y deberes, rutas de atención y trámites ante las empresas de acueducto, energía, gas y aseo.
            </p>
        """, unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        if c1.button("Ver empresas prestadoras", key="btn_emp_home"): set_page('Empresas')
        if c2.button("Solicitar orientación", key="btn_ori_home"): set_page('Orientacion')

    with col_right:
        g1, g2 = st.columns(2)
        with g1:
            st.button("⚖️\n\nDerechos", key="card_der")
            st.button("🏢\n\nEmpresas", key="card_emp", on_click=lambda: set_page('Empresas'))
        with g2:
            st.button("🗺️\n\nRutas de atención", key="card_rut")
            st.button("ℹ️\n\nOrientación DSP", key="card_ori", on_click=lambda: set_page('Orientacion'))

elif st.session_state.page == 'Empresas':
    st.markdown("## 🏢 Empresas Prestadoras")
    st.write("Consulta el sitio oficial según el servicio que necesites.")
    
    empresas = [
        {"n": "EAAV", "d": "Acueducto y Alcantarillado", "l": "https://www.eaav.gov.co"},
        {"n": "EMSA", "d": "Electrificadora del Meta", "l": "https://www.emsa-esp.com.co"},
        {"n": "Llanogas S.A.", "d": "Gas Domiciliario", "l": "https://llanogas.com"},
        {"n": "Bioagrícola", "d": "Servicio de Aseo", "l": "https://www.bioagricoladellano.com.co"}
    ]
    
    for emp in empresas:
        st.markdown(f"""
            <div class="company-card">
                <div>
                    <strong style="font-size: 18px;">{emp['n']}</strong><br>
                    <span style="color: #666;">{emp['d']}</span>
                </div>
                <a href="{emp['l']}" target="_blank" style="text-decoration:none;">
                    <button style="padding: 10px 20px; border-radius: 10px; border: 1px solid #1e45a5; background: white; color: #1e45a5; cursor: pointer; font-weight: bold;">Ir al sitio</button>
                </a>
            </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == 'Orientacion':
    st.markdown("## 📞 Formulario de Orientación Ciudadana")
    with st.form("form_orientacion"):
        c1, c2 = st.columns(2)
        nombre = c1.text_input("Nombre completo *")
        email = c2.text_input("Correo electrónico *")
        
        t1, t2 = st.columns(2)
        tema = t1.selectbox("Tema de orientación *", ["Facturación", "Calidad del servicio", "Peticiones/Quejas", "Otros"])
        servicio = t2.selectbox("Servicio *", ["Acueducto", "Energía", "Gas", "Aseo"])
        
        asunto = st.text_input("Asunto *")
        desc = st.text_area("Descripción detallada del caso")
        
        acepta = st.checkbox("Declaro que comprendo que este canal es de orientación.")
        
        submit = st.form_submit_button("Enviar solicitud")
        if submit:
            if not nombre or not email:
                st.error("Por favor completa los campos obligatorios.")
            else:
                st.success("Solicitud recibida. Nos contactaremos contigo pronto.")

elif st.session_state.page == 'Noticias':
    st.markdown("## 📰 Noticias y comunicados")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("**Jornada de orientación**\n\nAtención en el barrio San Benito este viernes.")
    with c2:
        st.warning("**Interrupción de servicio**\n\nMantenimiento preventivo en la red eléctrica.")
    with c3:
        st.success("**Nueva Normativa**\n\nConsulta los cambios en la ley de servicios públicos.")

elif st.session_state.page == 'Contacto':
    st.markdown("## ✉️ Contacto")
    st.markdown("""
        **Dirección:** Alcaldía de Villavicencio - Piso 4<br>
        **Horario:** Lunes a Viernes, 8:00 a.m. - 5:00 p.m.<br>
        **Correo institucional:** serviciospublicos@villavicencio.gov.co
    """, unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
st.markdown(f"""
    <div style="margin-top: 50px; padding: 20px; border-top: 1px solid rgba(255,255,255,0.1); text-align: center; font-size: 12px; opacity: 0.6;">
        © 2026 Alcaldía de Villavicencio — Dirección de Servicios Públicos Domiciliarios<br>
        Sección actual: {st.session_state.page}
    </div>
""", unsafe_allow_html=True)
