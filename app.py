
import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="DSPD Villavicencio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. ESTILOS REFINADOS (Sin hacks complicados)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    .stApp {
        background-color: #2B5AC4 !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    /* Ocultamos la barra gris superior de Streamlit */
    header {display: none !important;}
    .main .block-container {padding-top: 2rem !important;}

    /* Estilo para el título institucional */
    .inst-title {
        font-weight: 800;
        font-size: 22px;
        line-height: 1;
        margin-bottom: 0px;
    }
    .inst-sub {
        color: #00B7FF;
        font-weight: 700;
        font-size: 14px;
        text-transform: uppercase;
        margin-top: 5px;
    }

    /* Hero Text con puente en aguamarina */
    .hero-title {
        font-size: clamp(30px, 5vw, 55px);
        font-weight: 800;
        line-height: 1.1;
        margin-top: 20px;
    }
    .aguamarina { color: #7FFFD4; }

    /* Botones blancos con texto azul */
    div.stButton > button {
        background-color: white !important;
        color: #2B5AC4 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        border: none !important;
        padding: 0.5rem 1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO (Usando columnas nativas para asegurar el logo)
# Usamos st.image que es la forma más segura de que Streamlit muestre la imagen
head_col1, head_col2 = st.columns([1, 6])

with head_col1:
    # Si tienes el archivo local, cambia la URL por "logo.png"
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_de_Villavicencio.png/512px-Escudo_de_Villavicencio.png", width=80)

with head_col2:
    st.markdown('<p class="inst-title">Dirección de Servicios Públicos Domiciliarios</p>', unsafe_allow_html=True)
    st.markdown('<p class="inst-sub">Alcaldía de Villavicencio</p>', unsafe_allow_html=True)

st.markdown("---") # Línea divisoria sutil

# 4. CUERPO DE LA PÁGINA
st.markdown(f"""
    <h1 class="hero-title">
        Somos el <span class="aguamarina">puente</span> entre la ciudadanía y los prestadores de servicios públicos domiciliarios
    </h1>
    <p style="font-size: 18px; opacity: 0.9;">
        Te orientamos sobre tus derechos y deberes, rutas de atención y trámites ante las empresas de acueducto, energía, gas y aseo.
    </p>
""", unsafe_allow_html=True)

# Botones
btn_col1, btn_col2, btn_spacer = st.columns([2, 2, 4])
with btn_col1:
    st.button("Ver empresas prestadoras")
with btn_col2:
    st.button("Solicitar orientación")
