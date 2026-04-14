import streamlit as st

# 1. CONFIGURACIÓN TÉCNICA
st.set_page_config(
    page_title="Dirección de Servicios Públicos - Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="https://www.villavicencio.gov.co/favicon.ico"
)

# 2. ESTILOS CSS PERSONALIZADOS (Réplica exacta de dspvillavo.netlify.app)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    /* Colores base del sitio anterior */
    :root {
        --brand: #2B5AC4;
        --accent: #00B7FF;
    }

    .stApp {
        background-color: var(--brand) !important;
        font-family: 'Montserrat', sans-serif;
        color: white;
    }

    /* Estilo de Tarjetas del sitio anterior */
    .card-site {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
    }
    
    .accent-title {
        color: var(--accent);
        font-weight: 700;
        text-transform: uppercase;
        font-size: 14px;
        letter-spacing: 1px;
    }

    h1, h2, h3 {
        color: white !important;
        font-weight: 800 !important;
    }

    /* Ajuste de botones para que parezcan enlaces del sitio original */
    .stButton>button {
        background-color: transparent;
        color: var(--accent);
        border: none;
        padding: 0;
        text-decoration: underline;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER (Mantenido fijo)
col_l, col_r = st.columns([1, 6])
with col_l:
    st.image("logo.png", width=90) # Usa tu logo local

with col_r:
    st.markdown("""
        <div style="margin-top: 5px;">
            <h1 style="margin: 0; font-size: 24px; line-height: 1.1;">Dirección de Servicios Públicos Domiciliarios</h1>
            <p style="color: #00B7FF; margin: 0; font-weight: 700; font-size: 14px; text-transform: uppercase;">Alcaldía de Villavicencio</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 4. SISTEMA DE NAVEGACIÓN (Secciones de la página anterior)
tabs = st.tabs(["🏠 Inicio", "❓ ¿Qué hacemos?", "🏢 Empresas", "🙋 Orientación", "📂 Documentos", "📰 Noticias"])

# --- SECCIÓN: INICIO ---
with tabs[0]:
    st.markdown("""
        <div style="padding: 20px 0;">
            <h2 style="font-size: 40px; margin-bottom: 10px;">Somos el puente entre la ciudadanía y los prestadores</h2>
            <p style="font-size: 18px; color: rgba(255,255,255,0.8); max-width: 800px;">
                Te orientamos sobre tus derechos y deberes, rutas de atención y somos el apoyo institucional para mejorar la calidad de los servicios públicos en Villavicencio.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("📍 Ubicación: Calle 40 No. 33-64 Centro | Horario: 8:00 a.m. – 5:00 p.m.")

# --- SECCIÓN: ¿QUÉ HACEMOS? ---
with tabs[1]:
    st.markdown("## ¿Qué hacemos?")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="card-site">
            <span class="accent-title">Misión</span>
            <p>Orientar a los usuarios en la defensa de sus derechos y cumplimiento de sus deberes frente a las empresas prestadoras.</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card-site">
            <span class="accent-title">Gestión</span>
            <p>Monitoreamos la calidad de los servicios de agua, energía, gas y aseo en toda la ciudad.</p>
        </div>""", unsafe_allow_html=True)

# --- SECCIÓN: EMPRESAS ---
with tabs[2]:
    st.markdown("## Empresas Prestadoras")
    st.write("Consulta y accede a los canales oficiales de cada entidad.")
    
    # Grid de empresas como en el sitio original
    emp_col1, emp_col2 = st.columns(2)
    empresas = [
        ("EAAV", "Acueducto y Alcantarillado", "https://www.eaav.gov.co/"),
        ("EMSA", "Electrificadora del Meta", "https://www.electrificadoradelmeta.com.co/"),
        ("Llanogas", "Gas Domiciliario", "https://www.llanogas.com/"),
        ("Bioagrícola", "Aseo y Limpieza", "https://www.bioagricoladelllano.com.co/")
    ]
    
    for i, (name, desc, link) in enumerate(empresas):
        target_col = emp_col1 if i % 2 == 0 else emp_col2
        with target_col:
            st.markdown(f"""<div class="card-site">
                <h3 style="margin:0;">{name}</h3>
                <p style="font-size:14px; color:rgba(255,255,255,0.7);">{desc}</p>
            </div>""", unsafe_allow_html=True)
            st.link_button(f"Ir al sitio de {name}", link)

# --- SECCIÓN: ORIENTACIÓN ---
with tabs[3]:
    st.markdown("## Canal de Orientación Ciudadana")
    st.write("Si no tienes claro a qué empresa acudir, escríbenos:")
    
    with st.form("form_orientacion"):
        col_f1, col_f2 = st.columns(2)
        nombre = col_f1.text_input("Nombre completo *")
        correo = col_f2.text_input("Correo electrónico *")
        tema = st.selectbox("Tema", ["Facturación", "Subsidios", "Medidor", "PQR", "Otro"])
        servicio = st.radio("Servicio", ["Agua", "Energía", "Gas", "Aseo"], horizontal=True)
        mensaje = st.text_area("Descripción de su solicitud")
        
        submitted = st.form_submit_button("Enviar Solicitud")
        if submitted:
            st.success("Su solicitud ha sido enviada al equipo de la Dirección.")

# --- SECCIÓN: DOCUMENTOS ---
with tabs[4]:
    st.markdown("## Documentos y Normatividad")
    docs = ["Formato PQR Orientativo", "Normatividad General", "Resoluciones DSP"]
    for d in docs:
        with st.expander(f"📄 {d}"):
            st.write(f"Consulta los detalles y descarga el archivo de {d}.")
            st.button(f"Ver / Descargar {d}")

# --- SECCIÓN: NOTICIAS ---
with tabs[5]:
    st.markdown("## Noticias y Comunicados")
    st.markdown("""
        <div class="card-site">
            <span class="accent-title">Aviso · 2026</span>
            <h3>Jornada de orientación sobre facturación</h3>
            <p>Próximamente estaremos en su barrio socializando los cambios en las tarifas.</p>
        </div>
    """, unsafe_allow_html=True)

# 5. FOOTER
st.markdown("""
    <div style="text-align: center; padding: 40px 0; color: rgba(255,255,255,0.5); font-size: 13px;">
        © 2026 Alcaldía de Villavicencio — Dirección de Servicios Públicos Domiciliarios.<br>
        Actualizado: Abril 2026
    </div>
""", unsafe_allow_html=True)
