# 7. SECCIÓN: ORIENTACIÓN (Formulario con Asunto y Checklist)
st.markdown('<div id="orientacion" class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Solicitar Orientación Ciudadana</h2>', unsafe_allow_html=True)

with st.form("orientacion_form"):
    st.write("Complete el siguiente formulario para recibir asesoría de nuestro equipo.")
    
    # Campos de texto
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        nombre = st.text_input("Nombre completo")
        email = st.text_input("Correo electrónico")
    
    with col_f2:
        asunto = st.text_input("Asunto de la consulta") # Campo nuevo
        servicio = st.selectbox("Servicio relacionado", ["Acueducto", "Energía", "Gas", "Aseo", "Otro"])
    
    mensaje = st.text_area("Describa su inquietud detalladamente")
    
    # Checklist obligatorio (Campo nuevo)
    aceptacion = st.checkbox("Declaro que comprendo que este canal es de orientación y que los trámites formales se realizan con la empresa prestadora correspondiente.")
    
    submit = st.form_submit_button("Enviar solicitud")
    
    if submit:
        if not aceptacion:
            st.error("Debe aceptar la declaración de comprensión para enviar la solicitud.")
        elif nombre and email and asunto and mensaje:
            # Aquí iría la lógica para procesar los datos
            st.success(f"¡Gracias {nombre}! Tu solicitud sobre '{asunto}' ha sido enviada exitosamente.")
        else:
            st.warning("Por favor, complete todos los campos obligatorios.")

st.markdown('</div>', unsafe_allow_html=True)
