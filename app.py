import streamlit as st
import os
from datetime import date

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="DSPD Villavicencio", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS INTEGRADO (Todo lo anterior + Nuevos Componentes)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    html { scroll-behavior: smooth; }
    .stApp { background-color: #2B5AC4 !important; color: white !important; font-family: 'Montserrat', sans-serif !important; }
    header {display: none !important;}
    .block-container { padding-top: 1.5rem !important; }

    /* --- ENCABEZADO --- */
    .header-wrap { display: flex; align-items: center; padding-bottom: 10px; border-bottom: 0.5px solid rgba(255,255,255,0.15); margin-bottom: 25px; }
    .header-text { display: flex; flex-direction: column; justify-content: center; margin-left: 15px; }
    .title-main { font-weight: 800; font-size: 22px; color: white; line-height: 1.1; margin: 0 !important; }
    .title-sub { font-weight: 600; font-size: 15px; color: #00B7FF; margin-top: 2px !important; }

    /* --- BOTONES HERO --- */
    .btn-hero-white { background-color: white; color: #2B5AC4; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: 700; font-size: 14px; margin-right: 10px; display: inline-block; }
    .btn-hero-outline { background-color: transparent; color: white; border: 1px solid white; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: 700; font-size: 14px; display: inline-block; }

    /* --- TARJETAS INDICADORES (Navegación Hero) --- */
    .card-nav { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 15px; padding: 30px; text-align: center; height: 120px; display: flex; align-items: center; justify-content: center; transition: 0.3s; cursor: pointer; }
    .card-nav:hover { background: rgba(255,255,255,0.2); border-color: #7FFFD4; }

    /* --- SECCIÓN ¿QUÉ HACEMOS? --- */
    .card-action { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); border-radius: 15px; padding: 25px; height: 100%; }
    .card-action h4 { color: white; font-weight: 800; margin-bottom: 10px; }
    .card-action p { font-size: 14px; opacity: 0.9; line-height: 1.4; }

    /* --- EMPRESAS --- */
    .badge { font-size: 10px; font-weight: 800; padding: 3px 10px; border-radius: 20px; text-transform: uppercase; color: white; margin-bottom: 8px; display: inline-block; }
    .badge-agua { background-color: #00B7FF; }
    .badge-energia { background-color: #FFD700; color: #333; }
    .badge-gas { background-color: #FF8C00; }
    .badge-aseo { background-color: #32CD32; }
    .empresa-card { background-color: white; border-radius: 14px; padding: 20px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; color: #2B5AC4; transition: 0.2s; }
    .btn-sitio { background-color: white; border: 1px solid #ddd; padding: 8px 15px; border-radius: 8px; color: #2B5AC4; text-decoration: none; font-weight: 700; font-size: 13px; }

    /* --- NOTICIAS --- */
    .news-card { background: rgba(255,255,255,0.1); border-radius: 15px; padding: 20px; border: 1px solid rgba(255,255,255,0.1); }
    .news-tag { font-size: 10px; background: rgba(0,183,255,0.3); padding: 2px 8px; border-radius: 10px; margin-bottom: 10px; display: inline-block; }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO (Logo + Títulos)
h_col1, h_col2 = st.columns([1, 8])
with h_col1:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=85)
    else:
        st.markdown("🏛️")
with h_col2:
    st.markdown("""
        <div class="header-text">
            <p class="title-main">Dirección de Servicios Públicos<br>Domiciliarios</p>
            <p class="title-sub">Alcaldía de Villavicencio</p>
        </div>
    """, unsafe_allow_html=True)

# 4. HERO SECTION (Rediseñado con botones y tarjetas)
st.markdown('<div style="padding: 20px 0;">', unsafe_allow_html=True)
col_hero_text, col_hero_cards = st.columns([1.2, 1])

with col_hero_text:
    st.markdown("""
        <h1 style="font-size: 44px; font-weight: 800; line-height: 1.1; margin-bottom: 15px;">
            Somos el <span style="color: #7FFFD4;">puente</span> entre la ciudadanía y los prestadores
        </h1>
        <p style="font-size: 16px; opacity: 0.9; margin-bottom: 25px; max-width: 500px;">
            Te orientamos sobre tus derechos y deberes ante las empresas de acueducto, energía, gas y aseo.
        </p>
        <div style="margin-bottom: 30px;">
            <a href="#empresas" class="btn-hero-white">Ver empresas prestadoras</a>
            <a href="#orientacion" class="btn-hero-outline">Solicitar orientación</a>
        </div>
    """, unsafe_allow_html=True)

with col_hero_cards:
    # Bloque de 4 tarjetas (Futuros indicadores)
    c_nav1, c_nav2 = st.columns(2)
    with c_nav1:
        st.markdown('<div class="card-nav"><b>Derechos</b></div>', unsafe_allow_html=True)
        st.markdown('<div style="margin-top:15px;"></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-nav"><b>Empresas</b></div>', unsafe_allow_html=True)
    with c_nav2:
        st.markdown('<div class="card-nav"><b>Rutas de atención</b></div>', unsafe_allow_html=True)
        st.markdown('<div style="margin-top:15px;"></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-nav"><b>Orientación DSPD</b></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5. SECCIÓN: ¿QUÉ HACEMOS?
st.markdown('<h2 class="section-title">¿Qué hacemos?</h2>', unsafe_allow_html=True)
q1, q2, q3 = st.columns(3)
with q1:
    st.markdown('<div class="card-action"><h4>Orientación ciudadana</h4><p>Atendemos consultas sobre facturación, subsidios, PQR y procedimientos ante las empresas prestadoras.</p></div>', unsafe_allow_html=True)
with q2:
    st.markdown('<div class="card-action"><h4>Articulación institucional</h4><p>Servimos de enlace entre la ciudadanía, la Alcaldía, Superservicios y las empresas locales.</p></div>', unsafe_allow_html=True)
with q3:
    st.markdown('<div class="card-action"><h4>Educación y cultura</h4><p>Promovemos el uso responsable de los servicios y campañas informativas en barrios y veredas.</p></div>', unsafe_allow_html=True)

# 6. SECCIÓN: EMPRESAS (Título actualizado)
st.markdown('<div id="empresas" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Empresas prestadoras en Villavicencio</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Consulta el sitio oficial según el servicio que necesites.</p>', unsafe_allow_html=True)

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

e1, e2 = st.columns(2)
with e1:
    empresa_card("EAAV", "Acueducto y Alcantarillado", "https://www.eaav.gov.co", "Agua", "badge-agua")
    empresa_card("EMSA", "Electrificadora del Meta", "https://www.emsa-esp.com.co", "Energía", "badge-energia")
with e2:
    empresa_card("Llanogas", "Gas Natural Domiciliario", "https://llanogas.com", "Gas", "badge-gas")
    empresa_card("Bioagrícola", "Aseo y Residuos", "https://www.bioagricoladelllano.com.co", "Aseo", "badge-aseo")
st.markdown('</div>', unsafe_allow_html=True)

# 7. SECCIÓN: CANAL DE ORIENTACIÓN (Título actualizado)
st.markdown('<div id="orientacion" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Canal de orientación ciudadana</h2>', unsafe_allow_html=True)
st.markdown('<p style="margin-bottom:20px; opacity:0.8;">Si no tienes claro a qué empresa acudir o requieres guía sobre un trámite, escríbenos.</p>', unsafe_allow_html=True)

with st.expander("ABRIR FORMULARIO DE ORIENTACIÓN", expanded=True):
    with st.form("form_final_v2"):
        asunto_f = st.text_input("Asunto de la consulta")
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            nombre_f = st.text_input("Nombre completo")
            correo_f = st.text_input("Correo electrónico")
        with col_f2:
            servicio_f = st.selectbox("Servicio", ["Acueducto", "Energía", "Gas", "Aseo", "Otro"])
            barrio_f = st.text_input("Barrio / Vereda")
        mensaje_f = st.text_area("Descripción")
        check = st.checkbox("Acepto la política de tratamiento de datos.")
        if st.form_submit_button("REGISTRAR CONSULTA"):
            if not check: st.warning("Debe aceptar los términos.")
            elif nombre_f and correo_f: st.success("✅ Solicitud recibida.")
st.markdown('</div>', unsafe_allow_html=True)

# 8. SECCIÓN: NOTICIAS Y COMUNICADOS
st.markdown('<div id="noticias" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Noticias y comunicados</h2>', unsafe_allow_html=True)
st.markdown('<p style="opacity:0.8; margin-bottom:25px;">Avisos, comunicados y noticias breves de la Dirección.</p>', unsafe_allow_html=True)

n1, n2, n3 = st.columns(3)
with n1:
    st.markdown('<div class="news-card"><span class="news-tag">Aviso</span><p style="font-size:12px; float:right;">Ejemplo - 2026</p><h4>Jornada de orientación</h4><p style="font-size:14px; opacity:0.8;">Espacio para anunciar jornadas de atención ciudadana.</p><a href="#" style="color:#7FFFD4; font-size:13px; text-decoration:none;">Ver más</a></div>', unsafe_allow_html=True)
with n2:
    st.markdown('<div class="news-card"><span class="news-tag">Comunicado</span><p style="font-size:12px; float:right;">Ejemplo - 2026</p><h4>Interrupciones de servicio</h4><p style="font-size:14px; opacity:0.8;">Información sobre mantenimientos o suspensiones temporales.</p><a href="#" style="color:#7FFFD4; font-size:13px; text-decoration:none;">Ver más</a></div>', unsafe_allow_html=True)
with n3:
    st.markdown('<div class="news-card"><span class="news-tag">Recordatorio</span><p style="font-size:12px; float:right;">Ejemplo - 2026</p><h4>Plazos para radicar PQR</h4><p style="font-size:14px; opacity:0.8;">Fechas límite y recomendaciones para los usuarios.</p><a href="#" style="color:#7FFFD4; font-size:13px; text-decoration:none;">Ver más</a></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 9. FOOTER
fecha_str = date.today().strftime("%Y-%m-%d")
st.markdown(f"""
    <div style="margin-top:60px; padding:40px 0; border-top:1px solid rgba(255,255,255,0.1); display:flex; justify-content:space-between;">
        <div style="font-size:14px; opacity:0.8;">
            📍 Carrera 33 # 24-35 Piso 6, Villavicencio<br>
            📧 serviciospublicos@villavicencio.gov.co
        </div>
        <div style="text-align:right; font-size:12px; opacity:0.6;">
            © 2026 Alcaldía de Villavicencio<br>
            <b>Actualizado: {fecha_str}</b>
        </div>
    </div>
""", unsafe_allow_html=True)
