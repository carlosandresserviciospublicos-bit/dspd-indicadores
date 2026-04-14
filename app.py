import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    page_icon="https://www.villavicencio.gov.co/favicon.ico"
)

# 2. ESTILOS GLOBALES (Réplica exacta de la imagen)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    /* Fondo Azul Sólido */
    .stApp {
        background-color: #2B5AC4 !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Encabezado */
    .header-container {
        display: flex;
        align-items: center;
        gap: 20px;
        padding: 20px 0;
        border-bottom: 1px solid rgba(255,255,255,0.2);
    }

    /* Tarjetas de Empresas/Noticias */
    .custom-card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .custom-card:hover {
        border-color: #00B7FF;
        background-color: rgba(255, 255, 255, 0.1);
    }

    /* Títulos */
    h1, h2, h3 { color: white !important; font-weight: 800 !important; }
    .accent-text { color: #00B7FF !important; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }

    /* Eliminar espacios sobrantes de Streamlit */
    .block-container { padding-top: 2rem !important; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER CON LOGO LOCAL
col1, col2 = st.columns([1, 6])
with col1:
    try:
        # Usamos tu archivo local logo.png
        st.image("logo.png", width=95)
    except:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png", width=90)

with col2:
    st.markdown("""
        <div style="margin-top: 5px;">
            <h1 style="margin: 0; font-size: 26px; line-height: 1.1;">
                Dirección de Servicios Públicos Domiciliarios
            </h1>
            <p class="accent-text" style="margin: 0; font-size: 15px;">
                Alcaldía de Villavicencio
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 4. NAVEGACIÓN
menu = ["Inicio", "Empresas", "Orientación", "Documentos", "Contacto"]
choice = st.tabs(menu)

# 5. CONTENIDO
with choice[0]: # Inicio
    st.markdown("### Bienvenid@")
    st.write("Portal de orientación ciudadana sobre servicios públicos.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
            <div class="custom-card">
                <h3>🏢 Empresas</h3>
                <p>Consulta información de EAAV, EMSA, Llanogas y Bioagrícola.</p>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
            <div class="custom-card">
                <h3>📂 Trámites</h3>
                <p>Guía paso a paso para solicitudes y reclamaciones.</p>
            </div>
        """, unsafe_allow_html=True)

with choice[1]: # Empresas
    st.markdown("### Prestadores de Servicios")
    # Ejemplo de listado
    for empresa in ["EAAV (Agua)", "EMSA (Energía)", "Llanogas (Gas)", "Bioagrícola (Aseo)"]:
        with st.expander(f"📌 {empresa}"):
            st.write(f"Información detallada sobre {empresa}...")
            st.button(f"Ver trámites {empresa}")

with choice[2]: # Orientación
    st.markdown("### Canal de Orientación")
    with st.container():
        st.text_input("Nombre")
        st.text_input("Correo")
        st.selectbox("Servicio", ["Acueducto", "Energía", "Gas", "Aseo"])
        st.text_area("Descripción")
        st.button("Enviar Reporte")

with choice[3]: # Documentos
    st.markdown("### Normatividad y Formatos")
    st.markdown("""
        <div class="custom-card">
            <p>📄 Formato PQR Orientativo</p>
            <p>📄 Guía de Derechos del Usuario</p>
        </div>
    """, unsafe_allow_html=True)

with choice[4]: # Contacto
    st.markdown("### Información Institucional")
    st.info("📍 Alcaldía de Villavicencio - Calle 40 No. 33-64 Centro")
    st.write("📞 Horario: Lunes a Viernes 8:00 am - 5:00 pm")

# 6. FOOTER
st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 12px;">
        © 2026 Alcaldía de Villavicencio — Dirección de Servicios Públicos Domiciliarios.
    </div>
""", unsafe_allow_html=True)
