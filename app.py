import streamlit as st
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. CSS INTEGRADO (Estilos institucionales y de tarjetas)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    html { scroll-behavior: smooth; }
    .stApp { 
        background-color: #2B5AC4 !important; 
        color: white !important; 
        font-family: 'Montserrat', sans-serif !important; 
    }
    header {display: none !important;}
    .block-container {padding-top: 1.5rem !important;}

    /* Encabezado */
    .inst-title { font-weight: 800; font-size: 24px; margin: 0; }
    .inst-sub { color: #00B7FF; font-weight: 700; font-size: 15px; text-transform: uppercase; }
    
    /* Secciones */
    .section-container { padding: 50px 0 20px 0; }
    .hero-title { font-size: clamp(32px, 5vw, 55px); font-weight: 800; margin-top: 20px; line-height: 1.1; }
    .aguamarina { color: #7FFFD4; }

    /* Tarjetas de Información (Documentos/Noticias) */
    .info-card {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 25px;
        height: 100%;
        transition: transform 0.3s;
    }
    .info-card:hover { transform: translateY(-5px); background: rgba(255, 255, 255, 0.15); }
    .info-card h4 { font-weight: 800; margin-bottom: 10px; font-size: 18px; color: #7FFFD4; }
    .info-link { color: #00B7FF; text-decoration: none; font-weight: 700; font-size: 14px; }

    /* Footer */
    .footer-text { 
        text-align: center; 
        margin-top: 80px; 
        padding: 40px 0; 
        opacity: 0.8; 
        font-size: 14px; 
        border-top: 1px solid rgba(255,255,255,0.1); 
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO INSTITUCIONAL
col_l, col_t = st.columns([1, 7])
with col_l:
    if os.path.exists("logo.png"): 
        st.image("logo.png", width=95)
with col_t:
    st.markdown('<p class="inst-title">Dirección de Servicios Públicos Domiciliarios</p>', unsafe_allow_html=True)
    st.markdown('<p class="inst-sub">Alcaldía de Villavicencio</p>', unsafe_allow_html=True)

st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.15);'>", unsafe_allow_html=True)

# 4. HERO SECTION
st.markdown(f"""
    <div id="inicio">
        <h1 class="hero-title">Somos el <span class="aguamarina">puente</span> entre la ciudadanía y los prestadores</h1>
        <p style="font-size: 20px; opacity: 0.9; margin-bottom: 30px;">
            Te orientamos sobre tus derechos y deberes, rutas de atención y trámites ante las empresas de acueducto, energía, gas y aseo.
        </p>
    </div>
""", unsafe_allow_html=True)

# 5. SOLICITAR ORIENTACIÓN (Con Asunto y Checklist)
st.markdown('<div id="orientacion" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 32px; font-weight: 800;">Solicitar Orientación Ciudadana</h2>', unsafe_allow_html=True)

col_form, col_cont = st.columns([2, 1])

with col_form:
    with st.form("orientacion_form"):
        asunto = st.text_input("Asunto de la consulta") 
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            nombre = st.text_input("Nombre completo")
            email = st.text_input("Correo electrónico")
        with col_f2:
            servicio = st.selectbox("Servicio relacionado", ["Acueducto", "Energía", "Gas", "Aseo", "Otro"])
        
        mensaje = st.text_area("Describa su inquietud detalladamente")
        
        # Checklist de declaración
        aceptacion = st.checkbox("Declaro que comprendo que este canal es de orientación y que los trámites formales se realizan con la empresa prestadora correspondiente.")
        
        submit = st.form_submit_button("Enviar solicitud")
        if submit:
            if not aceptacion:
                st.error("Debe marcar la casilla de declaración para continuar.")
            elif nombre and email and asunto and mensaje:
                st.success(f"¡Gracias {nombre}! Tu solicitud sobre '{asunto}' ha sido recibida.")
            else:
                st.warning("Por favor complete todos los campos.")

with col_cont:
    st.markdown("""
        <div style="background: rgba(255,255,255,0.05); padding: 25px; border-radius: 15px; border-left: 4px solid #7FFFD4;">
            <h4 style="margin-top:0;">Canales de Atención</h4>
            <p style="font-size: 15px;">📍 <b>Dirección:</b> Carrera 33 # 24-35 <br>Piso 6, Edificio Alcaldía</p>
            <p style="font-size: 15px;">📧 <b>Correo:</b> serviciospublicos@villavicencio.gov.co</p>
            <p style="font-size: 15px;">⏰ <b>Horario:</b> Lunes a Viernes<br>8:00 AM - 12:00 PM / 2:00 PM - 5:30 PM</p>
        </div>
    """, unsafe_allow_html=True)

# 6. DOCUMENTOS Y NOTICIAS (Basado en capturas)
st.markdown('<div class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 32px; font-weight: 800;">Documentos y noticias</h2>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""<div class="info-card">
        <h4>Formato de PQR</h4>
        <p>Modelo orientativo para que los usuarios formulen peticiones o recursos ante su empresa prestadora.</p>
        <a href="#" class="info-link">Ver / descargar</a>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""<div class="info-card">
        <h4>Normatividad General</h4>
        <p>Referencia a la legislación principal que regula los servicios públicos domiciliarios en Colombia.</p>
        <a href="#" class="info-link">Ver / descargar</a>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown("""<div class="info-card">
        <h4>Noticias y avisos</h4>
        <p>Espacio para informar sobre jornadas de atención, cambios en tarifas y temas de interés ciudadano.</p>
        <a href="#" class="info-link">Ver más</a>
    </div>""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 7. PIE DE PÁGINA FINAL
st.markdown("""
    <div class="footer-text">
        © 2026 Alcaldía de Villavicencio — Dirección de Servicios Públicos Domiciliarios.<br>
        <b>Actualizado: 2026-04-28</b>
    </div>
""", unsafe_allow_html=True)
