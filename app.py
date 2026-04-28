import streamlit as st
import os
from datetime import date

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="DSPD Villavicencio", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS INTEGRADO (Encabezado exacto + Mejoras de Interactividad)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    html { scroll-behavior: smooth; }
    .stApp { background-color: #2B5AC4 !important; color: white !important; font-family: 'Montserrat', sans-serif !important; }
    header {display: none !important;}
    .block-container { padding-top: 1.5rem !important; }

    /* --- ENCABEZADO IDÉNTICO A LA IMAGEN --- */
    .header-wrap {
        display: flex;
        align-items: center; 
        padding: 10px 0;
        margin-bottom: 25px;
        border-bottom: 0.5px solid rgba(255,255,255,0.15);
    }
    .header-logo { margin-right: 18px; }
    .header-text { display: flex; flex-direction: column; justify-content: center; }
    .title-main {
        font-weight: 800; font-size: 22px; color: white; line-height: 1.1;
        margin: 0 !important; padding: 0 !important;
    }
    .title-sub {
        font-weight: 600; font-size: 15px; color: #00B7FF;
        margin-top: 2px !important; padding: 0 !important;
    }

    /* --- MEJORAS DE ORDEN Y UTILIDAD --- */
    .section-container { padding: 60px 0 30px 0; }
    .section-title { font-size: 34px; font-weight: 800; margin-bottom: 5px; }
    .section-subtitle { font-size: 17px; color: #7FFFD4; font-weight: 600; margin-bottom: 35px; }

    /* Badges de Servicio */
    .badge {
        font-size: 10px; font-weight: 800; padding: 3px 10px; border-radius: 20px;
        text-transform: uppercase; color: white; margin-bottom: 8px; display: inline-block;
    }
    .badge-agua { background-color: #00B7FF; }
    .badge-energia { background-color: #FFD700; color: #333; }
    .badge-gas { background-color: #FF8C00; }
    .badge-aseo { background-color: #32CD32; }

    /* Tarjetas Blancas (Empresas) con Hover */
    .empresa-card {
        background-color: white; border-radius: 14px; padding: 20px;
        margin-bottom: 15px; display: flex; justify-content: space-between;
        align-items: center; color: #2B5AC4; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .empresa-card:hover { transform: translateY(-3px); }
    
    /* Tarjetas Azules (Documentos/Noticias) */
    .card-info {
        background: rgba(255,255,255,0.1); padding: 25px; border-radius: 15px; 
        border: 1px solid rgba(255,255,255,0.15); height: 100%; transition: 0.3s;
    }
    .card-info:hover { background: rgba(255,255,255,0.18); border-color: #7FFFD4; }

    .btn-sitio {
        background-color: white; border: 1px solid #ddd; padding: 8px 15px;
        border-radius: 8px; color: #2B5AC4; text-decoration: none;
        font-weight: 700; font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. RENDER DEL ENCABEZADO MEJORADO
st.markdown(f"""
    <div class="header-wrap">
        <div class="header-logo">
            <img src="https://raw.githubusercontent.com/CarlosAndresVelasquez/dspd-indicadores/main/logo.png" width="80">
        </div>
        <div class="header-text">
            <p class="title-main">Dirección de Servicios Públicos<br>Domiciliarios</p>
            <p class="title-sub">Alcaldía de Villavicencio</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. HERO SECTION
st.markdown("""
    <div id="inicio">
        <h1 style="font-size: 48px; font-weight: 800; line-height: 1.1; margin-top: 20px;">
            Somos el <span style="color: #7FFFD4;">puente</span> entre la ciudadanía y los prestadores
        </h1>
        <p style="font-size: 20px; opacity: 0.9; margin-bottom: 30px; max-width: 850px;">
            Te orientamos sobre tus derechos y deberes ante las empresas de acueducto, energía, gas y aseo.
        </p>
    </div>
""", unsafe_allow_html=True)

# 5. SECCIÓN: EMPRESAS (Utilidad Directa)
st.markdown('<div id="empresas" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Directorio de Prestadores</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Consulta sitios oficiales y trámites en línea</p>', unsafe_allow_html=True)

def empresa_card(nombre, sub, url, tipo, b_class):
    st.markdown(f"""
        <div class="empresa-card">
            <div class="empresa-info">
                <span class="badge {b_class}">{tipo}</span>
                <h4 style="margin:0; font-weight:800;">{nombre}</h4>
                <p style="margin:0; font-size:13px; color:#666;">{sub}</p>
            </div>
            <a href="{url}" target="_blank" class="btn-sitio">Ir al sitio</a>
        </div>
    """, unsafe_allow_html=True)

ce1, ce2 = st.columns(2)
with ce1:
    empresa_card("EAAV", "Acueducto y Alcantarillado", "https://www.eaav.gov.co", "Agua", "badge-agua")
    empresa_card("EMSA", "Electrificadora del Meta", "https://www.emsa-esp.com.co", "Energía", "badge-energia")
with ce2:
    empresa_card("Llanogas", "Gas Natural Domiciliario", "https://llanogas.com", "Gas", "badge-gas")
    empresa_card("Bioagrícola", "Aseo y Residuos", "https://www.bioagricoladelllano.com.co", "Aseo", "badge-aseo")
st.markdown('</div>', unsafe_allow_html=True)

# 6. SECCIÓN: ORIENTACIÓN (Formulario con Barrio y Asunto)
st.markdown('<div id="orientacion" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Atención al Ciudadano</h2>', unsafe_allow_html=True)

with st.expander("ABRIR FORMULARIO DE ORIENTACIÓN", expanded=True):
    with st.form("form_final"):
        asunto = st.text_input("Asunto de la consulta")
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            nombre = st.text_input("Nombre completo")
            correo = st.text_input("Correo electrónico")
        with col_f2:
            servicio = st.selectbox("Servicio", ["Acueducto", "Energía", "Gas", "Aseo", "Otro"])
            barrio = st.text_input("Barrio / Vereda")
        mensaje = st.text_area("Descripción")
        check = st.checkbox("Acepto que este es un canal de orientación.")
        if st.form_submit_button("ENVIAR CONSULTA"):
            if not check: st.warning("Debe aceptar los términos.")
            elif nombre and correo: st.success("✅ Solicitud recibida.")
st.markdown('</div>', unsafe_allow_html=True)

# 7. DOCUMENTOS Y NOTICIAS (Basado en imagen 2)
st.markdown('<div id="documentos" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Documentos y Normatividad</h2>', unsafe_allow_html=True)
cd1, cd2, cd3 = st.columns(3)
with cd1:
    st.markdown('<div class="card-info"><h4>Formato PQR</h4><p>Modelo para radicar ante las empresas.</p><a href="#" style="color:#00B7FF; font-weight:700; text-decoration:none;">Descargar</a></div>', unsafe_allow_html=True)
with cd2:
    st.markdown('<div class="card-info"><h4>Normatividad</h4><p>Leyes de servicios públicos.</p><a href="#" style="color:#00B7FF; font-weight:700; text-decoration:none;">Ver más</a></div>', unsafe_allow_html=True)
with cd3:
    st.markdown('<div class="card-info"><h4>Resoluciones</h4><p>Actos administrativos DSP.</p><a href="#" style="color:#00B7FF; font-weight:700; text-decoration:none;">Consultar</a></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 8. FOOTER
hoy = date.today().strftime("%Y-%m-%d")
st.markdown(f"""
    <div style="margin-top:60px; padding:40px 0; border-top:1px solid rgba(255,255,255,0.1); display:flex; justify-content:space-between;">
        <div style="font-size:14px; opacity:0.8;">
            📍 Carrera 33 # 24-35 Piso 6, Villavicencio<br>
            📧 serviciospublicos@villavicencio.gov.co
        </div>
        <div style="text-align:right; font-size:12px; opacity:0.6;">
            © 2026 Alcaldía de Villavicencio<br>
            <b>Actualizado: {hoy}</b>
        </div>
    </div>
""", unsafe_allow_html=True)
