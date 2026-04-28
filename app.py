import streamlit as st
import os
from datetime import date # Importación necesaria para la fecha

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="DSPD Villavicencio", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS INTEGRADO Y MEJORADO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    html { scroll-behavior: smooth; }
    .stApp { background-color: #2B5AC4 !important; color: white !important; font-family: 'Montserrat', sans-serif !important; }
    header {display: none !important;}
    .block-container {padding-top: 1.5rem !important;}

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
    }
    .empresa-info h4 { margin: 0; font-weight: 800; color: #2B5AC4; font-size: 17px; }
    .empresa-info p { margin: 5px 0 0 0; font-size: 13px; color: #666; }
    
    .btn-sitio {
        background-color: white;
        border: 1px solid #ddd;
        padding: 8px 15px;
        border-radius: 8px;
        color: #2B5AC4;
        text-decoration: none;
        font-weight: 700;
        font-size: 13px;
    }

    /* Tarjetas de Información (Azules) */
    .card-info {
        background: rgba(255,255,255,0.1); 
        padding: 25px; 
        border-radius: 15px; 
        border: 1px solid rgba(255,255,255,0.15);
        height: 100%;
    }
    .card-info h4 { font-weight: 800; margin-bottom: 12px; font-size: 18px; }
    .card-info p { font-size: 14px; opacity: 0.85; margin-bottom: 15px; }
    .link-action { color: #00B7FF; text-decoration: none; font-weight: 700; font-size: 14px; }

    /* Secciones */
    .section-container { padding: 60px 0 30px 0; }
    .section-title { font-size: 34px; font-weight: 800; margin-bottom: 5px; }
    .section-subtitle { font-size: 16px; opacity: 0.8; margin-bottom: 35px; }

    /* Footer */
    .footer-box { 
        margin-top: 60px; 
        padding: 40px 0; 
        border-top: 1px solid rgba(255,255,255,0.15); 
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO
col_logo, col_titulo = st.columns([1, 7])
with col_logo:
    if os.path.exists("logo.png"): st.image("logo.png", width=95)
with col_titulo:
    st.markdown('<p class="inst-title">Dirección de Servicios Públicos Domiciliarios</p>', unsafe_allow_html=True)
    st.markdown('<p class="inst-sub">Alcaldía de Villavicencio</p>', unsafe_allow_html=True)

st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.15); margin-top: 10px;'>", unsafe_allow_html=True)

# 4. HOME / HERO
st.markdown(f"""
    <div id="inicio">
        <h1 class="hero-title">Somos el <span class="aguamarina">puente</span> entre la ciudadanía y los prestadores</h1>
        <p style="font-size: 20px; opacity: 0.9; margin-bottom: 30px; max-width: 850px;">
            Te orientamos sobre tus derechos y deberes, rutas de atención y trámites ante las empresas de acueducto, energía, gas y aseo.
        </p>
    </div>
""", unsafe_allow_html=True)

# 5. SECCIÓN: ¿QUÉ HACEMOS?
st.markdown("""
    <div id="que-hacemos" class="section-container">
        <h2 class="section-title">¿Qué hacemos?</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
            <div class="card-info">
                <h4>Orientación ciudadana</h4>
                <p>Atendemos consultas sobre facturación, subsidios, PQR y procedimientos ante las empresas prestadoras.</p>
            </div>
            <div class="card-info">
                <h4>Articulación institucional</h4>
                <p>Servimos de enlace entre la ciudadanía, la Alcaldía, Superservicios y las empresas locales.</p>
            </div>
            <div class="card-info">
                <h4>Educación y cultura</h4>
                <p>Promovemos el uso responsable de los servicios y campañas informativas en barrios y veredas.</p>
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

ce1, ce2 = st.columns(2)
with ce1:
    empresa_card("EAAV", "Acueducto y Alcantarillado", "https://www.eaav.gov.co")
    empresa_card("Llanogas S.A. E.S.P.", "Gas Natural", "https://llanogas.com")
    empresa_card("Superservicios", "Superintendencia de Servicios", "https://www.superservicios.gov.co")
with ce2:
    empresa_card("EMSA", "Electrificadora del Meta S.A.", "https://www.emsa-esp.com.co")
    empresa_card("Bioagrícola del Llano", "Aseo y Residuos", "https://www.bioagricoladelllano.com.co")
    empresa_card("Sisbén IV", "Portal oficial", "https://www.sisben.gov.co")
st.markdown('</div>', unsafe_allow_html=True)

# 7. SECCIÓN: ORIENTACIÓN (Formulario con Asunto y Checklist)
st.markdown('<div id="orientacion" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Solicitar Orientación Ciudadana</h2>', unsafe_allow_html=True)

with st.form("orientacion_form"):
    asunto = st.text_input("Asunto de la consulta")
    f1, f2 = st.columns(2)
    with f1:
        nombre = st.text_input("Nombre completo")
        correo = st.text_input("Correo electrónico")
    with f2:
        servicio = st.selectbox("Servicio relacionado", ["Acueducto", "Energía", "Gas", "Aseo", "Otro"])
        barrio = st.text_input("Barrio / Comuna")
    
    mensaje = st.text_area("Describa su inquietud detalladamente")
    check = st.checkbox("Declaro que comprendo que este canal es de orientación y que los trámites formales se realizan con la empresa prestadora correspondiente.")
    
    if st.form_submit_button("REGISTRAR CONSULTA"):
        if not check:
            st.error("Debe aceptar la declaración de comprensión.")
        elif nombre and correo and asunto:
            st.success("¡Gracias! Tu solicitud ha sido recibida exitosamente.")
st.markdown('</div>', unsafe_allow_html=True)

# 8. SECCIÓN: DOCUMENTOS Y NORMATIVIDAD
st.markdown('<div id="documentos" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Documentos y normatividad</h2>', unsafe_allow_html=True)

cd1, cd2, cd3 = st.columns(3)
with cd1:
    st.markdown('<div class="card-info"><h4>Formato de PQR</h4><p>Modelo para formular peticiones ante la empresa prestadora.</p><a href="#" class="link-action">Ver / descargar</a></div>', unsafe_allow_html=True)
with cd2:
    st.markdown('<div class="card-info"><h4>Normatividad General</h4><p>Legislación que regula los servicios públicos en Colombia.</p><a href="#" class="link-action">Ver / descargar</a></div>', unsafe_allow_html=True)
with cd3:
    st.markdown('<div class="card-info"><h4>Actos Administrativos</h4><p>Resoluciones expedidas por la Dirección de Servicios Públicos.</p><a href="#" class="link-action">Ver / descargar</a></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 9. SECCIÓN: NOTICIAS Y COMUNICADOS
st.markdown('<div id="noticias" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Noticias y comunicados</h2>', unsafe_allow_html=True)

cn1, cn2, cn3 = st.columns(3)
with cn1:
    st.markdown('<div class="card-info"><h4>Jornadas de Atención</h4><p>Anuncios de jornadas de orientación en barrios y veredas.</p><a href="#" class="link-action">Ver más</a></div>', unsafe_allow_html=True)
with cn2:
    st.markdown('<div class="card-info"><h4>Avisos de Interrupción</h4><p>Información sobre mantenimientos programados de servicios.</p><a href="#" class="link-action">Ver más</a></div>', unsafe_allow_html=True)
with cn3:
    st.markdown('<div class="card-info"><h4>Plazos de Facturación</h4><p>Fechas límite y recomendaciones para el pago de facturas.</p><a href="#" class="link-action">Ver más</a></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 10. PIE DE PÁGINA (Contacto y Legal)
hoy = date.today().strftime("%Y-%m-%d") # Forma correcta de obtener la fecha
st.markdown(f"""
    <div class="footer-box">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
            <div>
                <p><b>Contacto:</b><br>
                📍 Carrera 33 # 24-35 Piso 6, Edificio Alcaldía<br>
                📧 serviciospublicos@villavicencio.gov.co<br>
                ⏰ Lunes a Viernes: 8:00 AM - 12:00 PM / 2:00 PM - 5:30 PM</p>
            </div>
            <div style="text-align: right; opacity: 0.8;">
                <p>© 2026 Alcaldía de Villavicencio — Dirección de Servicios Públicos.<br>
                <b>Última actualización: {hoy}</b></p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
