import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="https://www.villavicencio.gov.co/favicon.ico"
)

# 2. ESTILOS GLOBALES (Réplica del sitio original)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;800&display=swap');
    
    /* Fondo y Fuente General */
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Títulos y Subtítulos */
    h1, h2, h3 { font-family: 'Montserrat', sans-serif !important; }
    
    /* Tarjetas de Navegación Estilo Glass */
    .nav-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        transition: transform 0.3s ease;
        cursor: pointer;
        margin-bottom: 20px;
    }
    .nav-card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid #00B7FF;
    }

    /* Estilo de Botones */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: transparent;
        color: white;
        border: 1px solid rgba(255,255,255,0.2);
        padding: 10px;
        font-weight: 600;
    }
    .stButton>button:hover {
        border-color: #00B7FF;
        color: #00B7FF;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO (Identidad Visual)
col_header1, col_header2 = st.columns([1, 5])
with col_header1:
    try:
        st.image("logo.png", width=100)
    except:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png", width=90)

with col_header2:
    st.markdown("""
        <div style="margin-top: 10px;">
            <h1 style="color: white; margin: 0; font-size: 28px; font-weight: 800; line-height: 1;">
                Dirección de Servicios Públicos Domiciliarios
            </h1>
            <p style="color: #00B7FF; margin: 0; font-size: 16px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                Alcaldía de Villavicencio
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border-top: 1px solid rgba(255,255,255,0.1);'>", unsafe_allow_html=True)

# 4. NAVEGACIÓN (Menú de Selección)
menu = ["Inicio", "Empresas", "Orientación", "Documentos", "Noticias", "Contacto"]
choice = st.radio("", menu, horizontal=True, label_visibility="collapsed")

# 5. CONTENIDO POR SECCIONES
if choice == "Inicio":
    st.markdown("## Bienvenid@")
    st.info("Este portal es una herramienta de orientación para los ciudadanos sobre los servicios públicos de Villavicencio.")
    
    # Grid de accesos rápidos
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="nav-card"><h3>🏢 Empresas</h3><p>Conoce los prestadores</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="nav-card"><h3>📂 Trámites</h3><p>Guía de orientación</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="nav-card"><h3>📰 Noticias</h3><p>Últimos boletines</p></div>', unsafe_allow_html=True)

elif choice == "Empresas":
    st.markdown("## Empresas Prestadoras")
    empresas = [
        {"nombre": "EAAV", "desc": "Agua y Alcantarillado", "web": "https://www.eaav.gov.co/"},
        {"nombre": "EMSA", "desc": "Energía Eléctrica", "web": "https://www.electrificadoradelmeta.com.co/"},
        {"nombre": "Llanogas", "desc": "Gas Domiciliario", "web": "https://www.llanogas.com/"},
        {"nombre": "Bioagrícola", "desc": "Aseo y Limpieza", "web": "https://www.bioagricoladelllano.com.co/"}
    ]
    for emp in empresas:
        with st.expander(f"📌 {emp['nombre']} - {emp['desc']}"):
            st.write(f"Para trámites de facturación y servicios de {emp['desc'].lower()}.")
            st.link_button("Ir al sitio oficial", emp['web'])

elif choice == "Orientación":
    st.markdown("## Formulario de Orientación")
    st.write("Si requieres guía sobre un trámite, completa los datos:")
    with st.form("orientacion_form"):
        col1, col2 = st.columns(2)
        nombre = col1.text_input("Nombre completo *")
        correo = col2.text_input("Correo electrónico *")
        tema = st.selectbox("Tema de orientación", ["Facturación", "Subsidios", "Consumos", "PQR", "Otro"])
        mensaje = st.text_area("Descripción de su solicitud")
        enviado = st.form_submit_button("Enviar Solicitud")
        if enviado:
            st.success("Solicitud enviada. Nos comunicaremos pronto.")

elif choice == "Documentos":
    st.markdown("## Documentos y Normatividad")
    st.download_button("Descargar Formato PQR", "Contenido ejemplo", file_name="pqr_modelo.pdf")
    st.markdown("- Resolución de Tarifas 2024")
    st.markdown("- Manual del Usuario")

elif choice == "Noticias":
    st.markdown("## Noticias y Comunicados")
    st.warning("⚠️ Mantenimiento programado: Sector Centro - 15 de Abril")
    st.write("La EAAV informa suspensión temporal por arreglo de tubería.")

elif choice == "Contacto":
    st.markdown("## Contacto")
    st.write("📍 **Ubicación:** Alcaldía de Villavicencio")
    st.write("⏰ **Horario:** Lunes a Viernes, 8:00 a.m. – 5:00 p.m.")
    st.write("📧 **Email:** serviciospublicos@villavicencio.gov.co")

# 6. PIE DE PÁGINA
st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 12px; color: #94a3b8;">
        © 2026 Alcaldía de Villavicencio — Dirección de Servicios Públicos Domiciliarios.
    </div>
""", unsafe_allow_html=True)
