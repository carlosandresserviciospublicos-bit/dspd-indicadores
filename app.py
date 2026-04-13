import streamlit as st

# Configuración de pantalla
st.set_page_config(page_title="DSPD - Indicadores", layout="wide")

# Diseño visual (Azul institucional)
st.markdown("""
    <style>
    .stApp { background-color: #2b59c3; color: white; }
    .stButton>button {
        width: 100%; height: 180px; border-radius: 15px;
        background-color: rgba(255,255,255,0.1); color: white;
        font-size: 22px; font-weight: bold; border: 2px solid rgba(255,255,255,0.2);
    }
    .stButton>button:hover { background-color: rgba(255,255,255,0.2); border: 2px solid white; }
    h1, h2, h3, p, span { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.title("Dirección de Servicios Públicos")
st.write("Sistema de Control de Indicadores - Alcaldía de Villavicencio")

# Los 4 botones tipo "Card" de tu imagen
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1: st.button("Derechos")
with col2: st.button("Rutas de atención")
with col3: st.button("Empresas")
with col4: st.button("Orientación DSP")

st.divider()
st.write("Página en construcción. Próximamente visualización de indicadores.")
