import streamlit as st
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="DSPD Villavicencio", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS PARA NAVEGACIÓN Y SECCIONES
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    html { scroll-behavior: smooth; } /* Desplazamiento suave */
    
    .stApp { background-color: #2B5AC4 !important; color: white !important; font-family: 'Montserrat', sans-serif !important; }
    header {display: none !important;}

    /* Encabezado */
    .inst-title { font-weight: 800; font-size: 24px; line-height: 1.1; margin: 0; }
    .inst-sub { color: #00B7FF; font-weight: 700; font-size: 15px; text-transform: uppercase; margin-top: 4px; }

    /* Hero */
    .hero-title { font-size: clamp(32px, 5vw, 55px); font-weight: 800; line-height: 1.1; margin-top: 20px; }
    .aguamarina { color: #7FFFD4; }

    /* Tarjetas de Empresas (Blancas) */
    .empresa-card {
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #2B5AC4;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .empresa-info h4 { margin: 0; font-weight: 800; color: #2B5AC4; }
    .empresa-info p { margin: 5px 0 0 0; font-size: 14px; color: #666; }
    
    .btn-sitio {
        background-color: white;
        border: 1px solid #ddd;
        padding: 8px 15px;
        border-radius: 8px;
        color: #2B5AC4;
        text-decoration: none;
        font-weight: 700;
        font-size: 14px;
    }

    /* Secciones */
    .section-container { padding: 60px 0 20px 0; }
    .section-title { font-size: 32px; font-weight: 800; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO
col_logo, col_titulo = st.columns([1, 7])
with col_logo:
    if os.path.exists("logo.png"): st.image("logo.png", width=95)
with col_titulo:
    st.markdown('<p class="inst-title">Dirección de Servicios Públicos Domiciliarios</p>', unsafe_allow_html=True)
    st.markdown('<p class="inst-sub">Alcaldía de Villavicencio</p>', unsafe_allow_html=True)

st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.15);'>", unsafe_allow_html=True)

# 4. HOME / HERO
st.markdown(f"""
    <div id="inicio">
        <h1 class="hero-title">Somos el <span class="aguamarina">puente</span> entre la ciudadanía y los prestadores</h1>
        <p style="font-size: 20px; opacity: 0.9; margin-bottom: 30px;">
            Te orientamos sobre tus derechos y deberes, rutas de atención y trámites ante las empresas de acueducto, energía, gas y aseo.
        </p>
    </div>
""", unsafe_allow_html=True)

# Botones rápidos
c1, c2, _ = st.columns([2.5, 2.5, 5])
with c1: 
    if st.button("Ver empresas prestadoras"):
        st.markdown('<script>window.location.href="#empresas";</script>', unsafe_allow_html=True)
with c2: 
    st.button("Solicitar orientación")

# 5. SECCIÓN: ¿QUÉ HACEMOS?
st.markdown("""
    <div id="que-hacemos" class="section-container">
        <h2 class="section-title">¿Qué hacemos?</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
            <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
                <h4 style="font-weight: 800;">Orientación ciudadana</h4>
                <p style="font-size: 14px; opacity: 0.8;">Atendemos consultas sobre facturación, subsidios, PQR y procedimientos ante las empresas prestadoras.</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
                <h4 style="font-weight: 800;">Articulación institucional</h4>
                <p style="font-size: 14px; opacity: 0.8;">Servimos de enlace entre la ciudadanía, la Alcaldía, Superservicios y las empresas locales.</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
                <h4 style="font-weight: 800;">Educación y cultura</h4>
                <p style="font-size: 14px; opacity: 0.8;">Promovemos el uso responsable de los servicios y campañas informativas en barrios y veredas.</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 6. SECCIÓN: EMPRESAS PRESTADORAS
st.markdown('<div id="empresas" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Empresas prestadoras en Villavicencio</h2>', unsafe_allow_html=True)

def empresa_card(nombre, sub, url):
    st.markdown(f"""
        <div class="empresa-card">
            <div class="empresa-info">
                <h4>{nombre}</h4>
                <p>{sub}</p>
            </div>
            <a href="{url}" target="_blank" class="btn-sitio">Ir al sitio</a>
        </div>
    """, unsafe_allow_html=True)

col_e1, col_e2 = st.columns(2)
with col_e1:
    empresa_card("EAAV", "Empresa de Acueducto y Alcantarillado", "https://www.eaav.gov.co")
    empresa_card("Llanogas S.A. E.S.P.", "Sitio oficial", "https://llanogas.com")
    empresa_card("Superservicios", "Superintendencia de Servicios Públicos", "https://www.superservicios.gov.co")
with col_e2:
    empresa_card("EMSA", "Electrificadora del Meta", "https://www.emsa-esp.com.co")
    empresa_card("Bioagrícola del Llano", "Sitio oficial", "https://www.bioagricoladelllano.com.co")
    empresa_card("Sisbén IV", "Portal oficial", "https://www.sisben.gov.co")

st.markdown('</div>', unsafe_allow_html=True)

# 7. SECCIÓN: ORIENTACIÓN (Formulario)
st.markdown('<div id="orientacion" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Solicitar Orientación</h2>', unsafe_allow_html=True)
with st.form("orientacion_form"):
    st.write("Déjanos tus datos y nos pondremos en contacto.")
    nombre = st.text_input("Nombre completo")
    email = st.text_input("Correo electrónico")
    servicio = st.selectbox("Servicio sobre el que consulta", ["Acueducto", "Energía", "Gas", "Aseo", "Otro"])
    mensaje = st.text_area("Describa su consulta o inquietud")
    submit = st.form_submit_button("Enviar solicitud")
    if submit:
        st.success("¡Gracias! Tu solicitud ha sido enviada.")
st.markdown('</div>', unsafe_allow_html=True)
