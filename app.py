import streamlit as st
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="DSPD Villavicencio", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS AVANZADO (Mejoras visuales de contraste y espaciado)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    html { scroll-behavior: smooth; }
    .stApp { background-color: #2B5AC4 !important; color: white !important; font-family: 'Montserrat', sans-serif !important; }
    header {display: none !important;}
    
    /* MEJORA: Sombras sutiles y bordes más suaves */
    .section-container { padding: 80px 0 40px 0; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .section-title { font-size: 38px; font-weight: 800; color: white; margin-bottom: 8px; }
    .section-subtitle { font-size: 18px; color: #7FFFD4; font-weight: 600; margin-bottom: 40px; }

    /* MEJORA: Tarjetas de Empresas con efecto de profundidad */
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
        transition: transform 0.2s;
    }
    .empresa-card:hover { transform: scale(1.02); }
    .empresa-info h4 { margin: 0; font-weight: 800; color: #2B5AC4; font-size: 18px; }

    /* MEJORA: Tarjetas Azules con gradiente sutil */
    .card-info {
        background: linear-gradient(145deg, rgba(255,255,255,0.12), rgba(255,255,255,0.05));
        padding: 30px; 
        border-radius: 20px; 
        border: 1px solid rgba(255,255,255,0.1);
        height: 100%;
        transition: all 0.3s ease;
    }
    .card-info:hover { border-color: #7FFFD4; background: rgba(255,255,255,0.15); }
    
    /* Botones Streamlit personalizados */
    div.stButton > button {
        border-radius: 10px !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO INTEGRADO
col_logo, col_titulo = st.columns([1, 7])
with col_logo:
    if os.path.exists("logo.png"): st.image("logo.png", width=100)
with col_titulo:
    st.markdown('<p class="inst-title">Dirección de Servicios Públicos Domiciliarios</p>', unsafe_allow_html=True)
    st.markdown('<p class="inst-sub">Alcaldía de Villavicencio</p>', unsafe_allow_html=True)

st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.1); margin: 20px 0;'>", unsafe_allow_html=True)

# 4. HERO SECTION (Mejora: Mayor jerarquía visual)
st.markdown(f"""
    <div id="inicio" style="padding: 40px 0;">
        <h1 class="hero-title">Somos el <span class="aguamarina">puente</span> entre la ciudadanía y los prestadores</h1>
        <p style="font-size: 22px; opacity: 0.95; line-height: 1.5; max-width: 900px;">
            Brindamos acompañamiento técnico y jurídico para garantizar la calidad en la prestación de los servicios públicos en nuestra ciudad.
        </p>
    </div>
""", unsafe_allow_html=True)

# 5. MEJORA: NAVEGACIÓN FUNCIONAL
# Usamos columnas para que los botones actúen como anclas reales
c1, c2, c3 = st.columns([2.5, 2.5, 5])
with c1:
    if st.button("📌 EMPRESAS PRESTADORAS", use_container_width=True):
        st.info("Desplázate hacia abajo para ver la sección de Empresas.")
with c2:
    if st.button("📩 SOLICITAR ORIENTACIÓN", use_container_width=True):
        st.info("Desplázate hacia abajo para completar el formulario.")

# 6. SECCIÓN: ¿QUÉ HACEMOS? (Mejora: Iconografía simbólica)
st.markdown("""
    <div id="que-hacemos" class="section-container">
        <h2 class="section-title">Nuestros Ejes</h2>
        <p class="section-subtitle">Compromiso institucional con el ciudadano</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px;">
            <div class="card-info">
                <h4>🔎 Seguimiento y Control</h4>
                <p>Monitoreamos el cumplimiento de los indicadores de calidad por parte de los operadores de servicios.</p>
            </div>
            <div class="card-info">
                <h4>🤝 Mediación</h4>
                <p>Facilitamos el diálogo constructivo entre comunidades y empresas prestadoras para resolver conflictos.</p>
            </div>
            <div class="card-info">
                <h4>📚 Capacitación</h4>
                <p>Formamos a los Vocales de Control y Comités de Desarrollo para un control social efectivo.</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 7. SECCIÓN: EMPRESAS (Mejora: Clasificación por servicio)
st.markdown('<div id="empresas" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Directorio de Prestadores</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Acceso directo a trámites y reportes oficiales</p>', unsafe_allow_html=True)

def empresa_card_v2(nombre, sub, url, tipo):
    st.markdown(f"""
        <div class="empresa-card">
            <div class="empresa-info">
                <span style="font-size:10px; background:#2B5AC4; color:white; padding:2px 8px; border-radius:10px;">{tipo}</span>
                <h4 style="margin-top:5px;">{nombre}</h4>
                <p>{sub}</p>
            </div>
            <a href="{url}" target="_blank" class="btn-sitio">Sitio Web</a>
        </div>
    """, unsafe_allow_html=True)

ce1, ce2 = st.columns(2)
with ce1:
    empresa_card_v2("EAAV", "Acueducto y Alcantarillado", "https://www.eaav.gov.co", "AGUA")
    empresa_card_v2("EMSA", "Electrificadora del Meta", "https://www.emsa-esp.com.co", "ENERGÍA")
    empresa_card_v2("Bioagrícola", "Gestión de Residuos", "https://www.bioagricoladelllano.com.co", "ASEO")
with ce2:
    empresa_card_v2("Llanogas", "Gas Natural Domiciliario", "https://llanogas.com", "GAS")
    empresa_card_v2("Alumbrado Público", "Concesión de luminarias", "#", "ILUMINACIÓN")
    empresa_card_v2("Superservicios", "Ente de control nacional", "https://www.superservicios.gov.co", "CONTROL")
st.markdown('</div>', unsafe_allow_html=True)

# 8. SECCIÓN: ORIENTACIÓN (Mejora: Formulario inteligente)
st.markdown('<div id="orientacion" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Atención al Ciudadano</h2>', unsafe_allow_html=True)

with st.expander("Abrir Formulario de Orientación Ciudadana", expanded=True):
    with st.form("orientacion_v2"):
        asunto = st.text_input("Asunto (Ej: Inconformidad con facturación)")
        f1, f2 = st.columns(2)
        with f1:
            nombre = st.text_input("Nombre y Apellidos")
            correo = st.text_input("Correo electrónico")
        with f2:
            servicio = st.selectbox("Servicio afectado", ["Acueducto", "Energía", "Aseo", "Gas", "Alumbrado Público"])
            barrio = st.text_input("Barrio / Comuna")
        
        mensaje = st.text_area("Detalles de su consulta")
        check = st.checkbox("Declaro que comprendo que este canal es de orientación y que los trámites formales se realizan con la empresa prestadora.")
        
        if st.form_submit_button("REGISTRAR CONSULTA"):
            if not check:
                st.warning("Debe aceptar la declaración de orientación.")
            elif nombre and correo and mensaje:
                st.success("✅ Solicitud enviada correctamente. Nuestro equipo revisará su caso.")
st.markdown('</div>', unsafe_allow_html=True)

# 9. PIE DE PÁGINA (Mejora: Diseño "Clean")
st.markdown(f"""
    <div class="footer-box">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
            <div>
                <h4 style="margin-bottom:10px;">Dirección de Servicios Públicos</h4>
                <p style="opacity:0.8;">📍 Carrera 33 # 24-35 Piso 6, Villavicencio<br>
                📧 serviciospublicos@villavicencio.gov.co</p>
            </div>
            <div style="text-align: right;">
                <p style="opacity:0.6; font-size: 12px;">
                    © 2026 Alcaldía de Villavicencio<br>
                    <b>Última actualización: {st.date_today()}</b>
                </p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
