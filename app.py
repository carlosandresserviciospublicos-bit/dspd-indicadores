import streamlit as st
import os
from datetime import date

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="DSPD Villavicencio", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS AVANZADO: INTERACTIVIDAD Y ORDEN VISUAL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    html { scroll-behavior: smooth; }
    
    /* Fondo y Fuente Base */
    .stApp { background-color: #2B5AC4 !important; color: white !important; font-family: 'Montserrat', sans-serif !important; }
    header {display: none !important;}

    /* Títulos y Subtítulos (Orden Visual) */
    .section-container { padding: 70px 0 30px 0; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .section-title { font-size: 38px; font-weight: 800; margin-bottom: 5px; color: white; }
    .section-subtitle { font-size: 18px; color: #7FFFD4; font-weight: 600; margin-bottom: 35px; }

    /* Tarjetas de Empresas (Interactividad Real) */
    .empresa-card {
        background-color: white;
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 18px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #2B5AC4;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .empresa-card:hover { transform: translateY(-3px); box-shadow: 0 6px 20px rgba(0,0,0,0.15); }
    .empresa-info h4 { margin: 0; font-weight: 800; color: #2B5AC4; font-size: 18px; }
    .empresa-info p { margin: 4px 0 0 0; font-size: 13px; color: #666; }
    
    /* Badges de Servicio (Utilidad Directa) */
    .badge {
        font-size: 10px; font-weight: 800; padding: 3px 10px; border-radius: 20px;
        text-transform: uppercase; color: white; margin-bottom: 8px; display: inline-block;
    }
    .badge-agua { background-color: #00B7FF; }
    .badge-energia { background-color: #FFD700; color: #333; }
    .badge-gas { background-color: #FF8C00; }
    .badge-aseo { background-color: #32CD32; }

    /* Tarjetas de Documentos/Noticias (Estilo Institucional) */
    .card-info {
        background: linear-gradient(145deg, rgba(255,255,255,0.12), rgba(255,255,255,0.05));
        padding: 30px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.15);
        height: 100%; transition: all 0.3s ease;
    }
    .card-info:hover { border-color: #7FFFD4; background: rgba(255,255,255,0.18); }
    
    .btn-sitio {
        background-color: white; border: 1px solid #ddd; padding: 10px 18px;
        border-radius: 10px; color: #2B5AC4; text-decoration: none;
        font-weight: 700; font-size: 13px; transition: 0.3s;
    }
    .btn-sitio:hover { background-color: #f8f9fa; border-color: #2B5AC4; }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO E INSTITUCIONALIDAD
col_logo, col_titulo = st.columns([1, 7])
with col_logo:
    if os.path.exists("logo.png"): st.image("logo.png", width=100)
with col_titulo:
    st.markdown('<p class="inst-title">Dirección de Servicios Públicos Domiciliarios</p>', unsafe_allow_html=True)
    st.markdown('<p class="inst-sub">Alcaldía de Villavicencio</p>', unsafe_allow_html=True)

st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.1); margin: 20px 0;'>", unsafe_allow_html=True)

# 4. HERO SECTION
st.markdown(f"""
    <div id="inicio" style="padding: 20px 0 40px 0;">
        <h1 class="hero-title">Somos el <span class="aguamarina">puente</span> entre la ciudadanía y los prestadores</h1>
        <p style="font-size: 22px; opacity: 0.95; line-height: 1.5; max-width: 900px;">
            Acompañamos a los villavicenses en la garantía de sus derechos y el cumplimiento de sus deberes frente a los servicios públicos.
        </p>
    </div>
""", unsafe_allow_html=True)

# 5. ¿QUÉ HACEMOS? (Mejora: Ejes de Acción)
st.markdown("""
    <div id="que-hacemos" class="section-container">
        <h2 class="section-title">Nuestros Ejes</h2>
        <p class="section-subtitle">Gestión transparente para la comunidad</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px;">
            <div class="card-info">
                <h4>🔎 Seguimiento</h4>
                <p>Verificamos que las empresas cumplan con la prestación eficiente de los servicios en toda la ciudad.</p>
            </div>
            <div class="card-info">
                <h4>🤝 Mediación</h4>
                <p>Orientamos al ciudadano en la resolución de conflictos y radicación de solicitudes ante los prestadores.</p>
            </div>
            <div class="card-info">
                <h4>📚 Control Social</h4>
                <p>Fortalecemos la participación ciudadana a través de la capacitación a Vocales de Control.</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 6. EMPRESAS (Mejora: Utilidad Directa con Badges)
st.markdown('<div id="empresas" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Directorio de Prestadores</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Consulta sitios oficiales y trámites en línea</p>', unsafe_allow_html=True)

def empresa_card_mejorada(nombre, sub, url, tipo, badge_class):
    st.markdown(f"""
        <div class="empresa-card">
            <div class="empresa-info">
                <span class="badge {badge_class}">{tipo}</span>
                <h4>{nombre}</h4>
                <p>{sub}</p>
            </div>
            <a href="{url}" target="_blank" class="btn-sitio">Ir al sitio</a>
        </div>
    """, unsafe_allow_html=True)

ce1, ce2 = st.columns(2)
with ce1:
    empresa_card_mejorada("EAAV", "Acueducto y Alcantarillado de Villavicencio", "https://www.eaav.gov.co", "Agua", "badge-agua")
    empresa_card_mejorada("EMSA", "Electrificadora del Meta", "https://www.emsa-esp.com.co", "Energía", "badge-energia")
    empresa_card_mejorada("Bioagrícola", "Gestión de Residuos y Aseo", "https://www.bioagricoladelllano.com.co", "Aseo", "badge-aseo")
with ce2:
    empresa_card_mejorada("Llanogas", "Gas Natural Domiciliario", "https://llanogas.com", "Gas", "badge-gas")
    empresa_card_mejorada("Sisbén IV", "Portal oficial de consultas", "https://www.sisben.gov.co", "Social", "badge-agua")
    empresa_card_mejorada("Superservicios", "Ente de Control Nacional", "https://www.superservicios.gov.co", "Control", "badge-gas")
st.markdown('</div>', unsafe_allow_html=True)

# 7. ORIENTACIÓN (Mejora: Utilidad Directa y Seguridad)
st.markdown('<div id="orientacion" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Solicitar Orientación Ciudadana</h2>', unsafe_allow_html=True)

with st.expander("📝 CLIC AQUÍ PARA ABRIR EL FORMULARIO DE CONSULTA", expanded=True):
    with st.form("orientacion_vfinal"):
        asunto_input = st.text_input("Asunto de su consulta (Ej: Reclamo por alta facturación)")
        f1, f2 = st.columns(2)
        with f1:
            nom_comp = st.text_input("Nombre completo")
            mail_comp = st.text_input("Correo electrónico")
        with f2:
            serv_comp = st.selectbox("Servicio relacionado", ["Acueducto", "Energía", "Gas", "Aseo", "Otros"])
            barrio_comp = st.text_input("Barrio o Vereda")
        
        mensaje_comp = st.text_area("Describa su inquietud")
        acepto_comp = st.checkbox("Entiendo que esta es una oficina de orientación y que la PQR formal se debe radicar ante la empresa.")
        
        if st.form_submit_button("REGISTRAR CONSULTA"):
            if not acepto_comp:
                st.warning("Debe aceptar la declaración para enviar.")
            elif nom_comp and mail_comp and asunto_input:
                st.success("✅ Solicitud registrada. Nos pondremos en contacto pronto.")
st.markdown('</div>', unsafe_allow_html=True)

# 8. DOCUMENTOS Y NOTICIAS (Orden Visual - Imagen 2)
st.markdown('<div id="documentos" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Documentos y Normatividad</h2>', unsafe_allow_html=True)
d1, d2, d3 = st.columns(3)
with d1:
    st.markdown('<div class="card-info"><h4>Formato PQR</h4><p>Modelo orientativo para radicar ante las empresas.</p><a href="#" style="color:#00B7FF; text-decoration:none; font-weight:700;">Descargar</a></div>', unsafe_allow_html=True)
with d2:
    st.markdown('<div class="card-info"><h4>Leyes y Decretos</h4><p>Compendio de normas sobre servicios públicos en Colombia.</p><a href="#" style="color:#00B7FF; text-decoration:none; font-weight:700;">Ver más</a></div>', unsafe_allow_html=True)
with d3:
    st.markdown('<div class="card-info"><h4>Resoluciones DSP</h4><p>Actos administrativos expedidos por esta Dirección.</p><a href="#" style="color:#00B7FF; text-decoration:none; font-weight:700;">Consultar</a></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 9. PIE DE PÁGINA (Contacto y Actualización)
hoy_fecha = date.today().strftime("%Y-%m-%d")
st.markdown(f"""
    <div style="margin-top:60px; padding:40px 0; border-top:1px solid rgba(255,255,255,0.1); display:flex; justify-content:space-between; flex-wrap:wrap;">
        <div style="font-size:14px; opacity:0.9;">
            <b>Dirección de Servicios Públicos Domiciliarios</b><br>
            📍 Carrera 33 # 24-35 Piso 6, Alcaldía de Villavicencio<br>
            📧 serviciospublicos@villavicencio.gov.co<br>
            ⏰ Lun-Vie: 8:00 AM - 12:00 PM / 2:00 PM - 5:30 PM
        </div>
        <div style="text-align:right; font-size:13px; opacity:0.7;">
            © 2026 Alcaldía de Villavicencio<br>
            <b>Última actualización: {hoy_fecha}</b>
        </div>
    </div>
""", unsafe_allow_html=True)
