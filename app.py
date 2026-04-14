import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="https://www.villavicencio.gov.co/favicon.ico"
)

# 2. ESTILOS GLOBALES (Enfoque en Azul Institucional y Montserrat)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;800&display=swap');
    
    /* Fondo Azul con Gradiente */
    .stApp {
        background: linear-gradient(135deg, #071333 0%, #0d2159 100%) !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Ajuste de color de texto para todos los componentes */
    h1, h2, h3, p, span, label { 
        color: white !important; 
        font-family: 'Montserrat', sans-serif !important; 
    }

    /* Tarjetas de Navegación Estilo Glass (Transparentes sobre azul) */
    .nav-card {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }
    .nav-card:hover {
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid #00B7FF;
        transform: translateY(-5px);
    }

    /* Estilo para los botones de Streamlit */
    .stButton>button {
        background-color: rgba(255, 255, 255, 0.1);
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 8px;
        font-weight: 600;
    }
    .stButton>button:hover {
        border-color: #00B7FF;
        color: #00B7FF !important;
    }

    /* Menú de radio horizontal personalizado */
    div[data-testid="stMarkdownContainer"] hr {
        border-top: 1px solid rgba(255, 255, 255, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO (Identidad Visual)
col_header1, col_header2 = st.columns([1, 5])
with col_header1:
    try:
        # Intenta usar el logo local que mencionaste que funciona
        st.image("logo.png", width=100)
    except:
        # Respaldo si no encuentra el archivo
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png", width=90)

with col_header2:
    st.markdown("""
        <div style="margin-top: 10px;">
            <h1 style="margin: 0; font-size: 28px; font-weight: 800; line-height: 1;">
                Dirección de Servicios Públicos Domiciliarios
            </h1>
            <p style="color: #00B7FF !important; margin: 0; font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px;">
                Alcaldía de Villavicencio
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 4. NAVEGACIÓN
menu = ["Inicio", "Empresas", "Orientación", "Documentos", "Noticias", "Contacto"]
# Usamos un contenedor para que el menú resalte sobre el azul
choice = st.radio("Navegación", menu, horizontal=True, label_visibility="collapsed")

# 5. CONTENIDO POR SECCIONES
if choice == "Inicio":
    st.markdown("## Bienvenid@")
    st.write("Portal oficial de orientación ciudadana sobre servicios públicos domiciliarios.")
    
    # Grid de accesos rápidos estilo tarjetas
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="nav-card"><h3>🏢 Empresas</h3><p>Directorio de prestadores</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="nav-card"><h3>📂 Trámites</h3><p>Guía de orientación ciudadana</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="nav-card"><h3>📰 Noticias</h3><p>Boletines y alertas</p></div>', unsafe_allow_html=True)

elif choice == "Empresas":
    st.markdown("## Empresas Prestadoras")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown('<div class="nav-card"><h4>EAAV</h4><p>Agua y Alcantarillado</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="nav-card"><h4>EMSA</h4><p>Energía Eléctrica</p></div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="nav-card"><h4>Llanogas</h4><p>Gas Domiciliario</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="nav-card"><h4>Bioagrícola</h4><p>Aseo y Limpieza</p></div>', unsafe_allow_html=True)

elif choice == "Orientación":
    st.markdown("## Canal de Orientación")
    with st.container():
        st.write("Complete el formulario para recibir guía técnica.")
        nombre = st.text_input("Nombre completo")
        correo = st.text_input("Correo electrónico")
        asunto = st.selectbox("Asunto", ["Facturación", "PQR", "Subsidios", "Otro"])
        mensaje = st.text_area("Descripción")
        if st.button("Enviar"):
            st.success("Mensaje recibido correctamente.")

elif choice == "Documentos":
    st.markdown("## Documentos y Normatividad")
    st.info("Aquí podrá consultar resoluciones y formatos oficiales.")
    st.button("Descargar Modelo PQR (PDF)")

elif choice == "Noticias":
    st.markdown("## Noticias")
    st.markdown("""
        <div class="nav-card" style="text-align: left;">
            <h4 style="color: #00B7FF !important;">Aviso importante</h4>
            <p>Jornada de socialización de tarifas en la Comuna 4 - Próximo lunes.</p>
        </div>
    """, unsafe_allow_html=True)

elif choice == "Contacto":
    st.markdown("## Información de Contacto")
    st.markdown("""
        <div class="nav-card">
            <p>📍 Calle 40 No. 33-64 Centro</p>
            <p>📧 dspd@villavicencio.gov.co</p>
            <p>⏰ Lunes a Viernes: 8:00 am - 5:00 pm</p>
        </div>
    """, unsafe_allow_html=True)

# 6. PIE DE PÁGINA
st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; font-size: 13px; color: rgba(255,255,255,0.5);">
        © 2026 Alcaldía de Villavicencio — Dirección de Servicios Públicos Domiciliarios.
    </div>
""", unsafe_allow_html=True)
