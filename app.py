import streamlit as st
import os
from datetime import date

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="DSPD Villavicencio", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS INTEGRADO (Encabezado de imagen + Estilos de Secciones)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    html { scroll-behavior: smooth; }
    .stApp { background-color: #2B5AC4 !important; color: white !important; font-family: 'Montserrat', sans-serif !important; }
    header {display: none !important;}
    .block-container { padding-top: 1.5rem !important; }

    /* --- ENCABEZADO IDÉNTICO A TU IMAGEN --- */
    .header-wrap {
        display: flex;
        align-items: center; 
        padding-bottom: 15px;
        margin-bottom: 25px;
        border-bottom: 0.5px solid rgba(255,255,255,0.15);
    }
    .header-text { display: flex; flex-direction: column; justify-content: center; margin-left: 15px; }
    .title-main {
        font-weight: 800; font-size: 22px; color: white; line-height: 1.1;
        margin: 0 !important; padding: 0 !important;
    }
    .title-sub {
        font-weight: 600; font-size: 15px; color: #00B7FF;
        margin-top: 2px !important; padding: 0 !important;
    }

    /* --- ESTILOS DE SECCIONES (Interactividad y Orden) --- */
    .section-container { padding: 60px 0 30px 0; }
    .section-title { font-size: 34px; font-weight: 800; margin-bottom: 10px; }
    .section-subtitle { font-size: 17px; color: #7FFFD4; font-weight: 600; margin-bottom: 35px; opacity: 0.9; }

    .badge {
        font-size: 10px; font-weight: 800; padding: 3px 10px; border-radius: 20px;
        text-transform: uppercase; color: white; margin-bottom: 8px; display: inline-block;
    }
    .badge-agua { background-color: #00B7FF; }
    .badge-energia { background-color: #FFD700; color: #333; }
    .badge-gas { background-color: #FF8C00; }
    .badge-aseo { background-color: #32CD32; }

    .empresa-card {
        background-color: white; border-radius: 14px; padding: 20px;
        margin-bottom: 15px; display: flex; justify-content: space-between;
        align-items: center; color: #2B5AC4; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .empresa-card:hover { transform: translateY(-3px); }
    
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

# 3. RENDER DEL ENCABEZADO (Corrección del Logo)
# Creamos un contenedor flex para el logo y el texto
header_col1, header_col2 = st.columns([1, 8])

with header_col1:
    # Esta función carga el archivo logo.png desde tu repositorio
    if os.path.exists("logo.png"):
        st.image("logo.png", width=85)
    else:
        # Si no lo encuentra, mostramos un aviso visual amigable
        st.markdown("🏛️")

with header_col2:
    st.markdown("""
        <div class="header-text">
            <p class="title-main">Dirección de Servicios Públicos<br>Domiciliarios</p>
            <p class="title-sub">Alcaldía de Villavicencio</p>
        </div>
    """, unsafe_allow_html=True)

# Línea divisoria sutil (opcional, integrada en el wrap arriba)
st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

# 4. HERO SECTION
st.markdown("""
    <div id="inicio">
        <h1 style="font-size: 48px; font-weight: 800; line-height: 1.1; margin-top: 10px;">
            Somos el <span style="color: #7FFFD4;">puente</span> entre la ciudadanía y los prestadores
        </h1>
        <p style="font-size: 20px; opacity: 0.9; margin-bottom: 30px; max-width: 850px;">
            Te orientamos sobre tus derechos y deberes ante las empresas de acueducto, energía, gas y aseo.
        </p>
    </div>
""", unsafe_allow_html=True)

# 5. SECCIÓN: EMPRESAS
st.markdown('<div id="empresas" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Directorio de Prestadores</h2>', unsafe_allow_html=True)

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

e_col1, e_col2 = st.columns(2)
with e_col1:
    empresa_card("EAAV", "Acueducto y Alcantarillado", "https://www.eaav.gov.co", "Agua", "badge-agua")
    empresa_card("EMSA", "Electrificadora del Meta", "https://www.emsa-esp.com.co", "Energía", "badge-energia")
with e_col2:
    empresa_card("Llanogas", "Gas Natural Domiciliario", "https://llanogas.com", "Gas", "badge-gas")
    empresa_card("Bioagrícola", "Aseo y Residuos", "https://www.bioagricoladelllano.com.co", "Aseo", "badge-aseo")
st.markdown('</div>', unsafe_allow_html=True)

# 6. SECCIÓN: ORIENTACIÓN
st.markdown('<div id="orientacion" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Atención al Ciudadano</h2>', unsafe_allow_html=True)

with st.expander("ABRIR FORMULARIO DE ORIENTACIÓN", expanded=True):
    with st.form("form_final_fixed"):
        asunto = st.text_input("Asunto de la consulta")
        f_col1, f_col2 = st.columns(2)
        with f_col1:
            nombre = st.text_input("Nombre completo")
            correo = st.text_input("Correo electrónico")
        with f_col2:
            servicio = st.selectbox("Servicio", ["Acueducto", "Energía", "Gas", "Aseo", "Otro"])
            barrio = st.text_input("Barrio / Vereda")
        mensaje = st.text_area("Descripción de su inquietud")
        check = st.checkbox("Declaro que he leído y acepto los términos de orientación ciudadana.")
        if st.form_submit_button("REGISTRAR CONSULTA"):
            if not check: st.warning("Por favor, acepte los términos para continuar.")
            elif nombre and correo: st.success("✅ Su solicitud ha sido registrada exitosamente.")
st.markdown('</div>', unsafe_allow_html=True)

# 7. DOCUMENTOS Y NOTICIAS
st.markdown('<div id="documentos" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Documentos y Normatividad</h2>', unsafe_allow_html=True)
doc_col1, doc_col2, doc_col3 = st.columns(3)
with doc_col1:
    st.markdown('<div class="card-info"><h4>Formato PQR</h4><p>Modelo orientativo para radicar ante las empresas.</p><a href="#" style="color:#00B7FF; font-weight:700; text-decoration:none;">Descargar</a></div>', unsafe_allow_html=True)
with doc_col2:
    st.markdown('<div class="card-info"><h4>Normatividad</h4><p>Leyes y decretos de servicios públicos.</p><a href="#" style="color:#00B7FF; font-weight:700; text-decoration:none;">Ver más</a></div>', unsafe_allow_html=True)
with doc_col3:
    st.markdown('<div class="card-info"><h4>Resoluciones</h4><p>Actos administrativos expedidos por la DSP.</p><a href="#" style="color:#00B7FF; font-weight:700; text-decoration:none;">Consultar</a></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 8. FOOTER
hoy_fecha = date.today().strftime("%Y-%m-%d")
st.markdown(f"""
    <div style="margin-top:60px; padding:40px 0; border-top:1px solid rgba(255,255,255,0.1); display:flex; justify-content:space-between; align-items:flex-end;">
        <div style="font-size:14px; opacity:0.8;">
            📍 Carrera 33 # 24-35 Piso 6, Alcaldía de Villavicencio<br>
            📧 serviciospublicos@villavicencio.gov.co<br>
            ⏰ Horario: 8:00 AM - 12:00 PM / 2:00 PM - 5:30 PM
        </div>
        <div style="text-align:right; font-size:12px; opacity:0.6;">
            © 2026 Alcaldía de Villavicencio<br>
            <b>Última actualización: {hoy_fecha}</b>
        </div>
    </div>
""", unsafe_allow_html=True)
