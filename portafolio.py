import streamlit as st

# Configurar la página
st.set_page_config(
    page_title="Portafolio de Miguel Caso",
    page_icon="🎤",
    layout="wide"
)

# Fondo con CSS personalizado
st.markdown("""
    <style>
    .stApp {
        background-image: url("fondo.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.93);
        padding: 2rem;
        border-radius: 12px;
        max-width: 1100px;
        margin: auto;
    }
    h1, h2, h3 {
        color: #3b3054;
    }
    </style>
""", unsafe_allow_html=True)

# Contenedor principal
with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center;'>🎤 Portafolio de Miguel Caso</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Imagen y presentación
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("mi_foto.jpg", caption="Miguel Caso", width=250)
        except:
            st.warning("⚠️ No se encontró la imagen 'mi_foto.jpg'.")
    with col2:
        st.markdown("### 👤 Sobre mi persona")
        st.write("""
Soy una persona apasionada por el arte y la creatividad. Me encanta cantar, componer canciones, inventar historias y expresarme a través de los instrumentos musicales.  
Encuentro en la música y la narrativa una forma de conectar con los demás y conmigo mismo.  
Creo firmemente en el esfuerzo como clave del crecimiento personal; para mí, no hay victoria sin sacrificio.  
Cada meta que me propongo la enfrento con disciplina, entrega y corazón, porque sé que los sueños solo se alcanzan cuando se trabaja por ellos con constancia y pasión.
        """)

    st.markdown("---")

    # Habilidades
    st.markdown("### 🎯 Habilidades")
    st.markdown("""
- 🖥️ Conocimientos de computación  
- 🎥 Conocimientos audiovisuales  
- 🧹 Realizar limpieza de espacios  
- 🤓 Aprendo diversas actividades con facilidad
    """)

    # Perfil
    st.markdown("### 🧩 Perfil Personal")
    st.markdown("""
- Estudiante universitario, cursando la carrera de Comunicación Audiovisual  
- Soy amigable con las personas que están en mi entorno  
- Aprendo con facilidad lo que me enseñan  
- Soy muy dedicado al trabajo que se me designa
    """)

    # Experiencia Laboral
    st.markdown("### 💼 Experiencia Laboral")
    st.markdown("""
- Cobrador de pasajes (vía electrónica) en la Empresa de Transporte Internacional ECO  
- Recojo y envío de encomiendas  
- Limpieza de buses interprovinciales  
- Producción de Entrevistas  
- Asesor de Experiencia en Cineplanet (Limpieza de Salas, Atención al cliente y Dulcería)  
- Atención al Cliente en un Restaurante (Limpieza, Mozo, Cocina y Delivery)
    """)

    # Proyecto
    st.markdown("### 🎬 Proyecto: *Entre Palabras*")
    st.write("""
**Entre Palabras** es un cortometraje realizado en colaboración con un grupo de amigos, que aborda la falta de valentía que puede surgir cuando alguien cree haber encontrado el amor.  
A través de una narrativa íntima y emocional, exploramos cómo el miedo a expresarse y la inseguridad pueden transformar lo que parecía una conexión sincera en un vacío profundo, cubierto por la soledad.  
Esta historia refleja cómo, entre palabras no dichas y sentimientos reprimidos, se desdibuja la posibilidad de un verdadero encuentro emocional.
    """)

    # Pasatiempos
    st.markdown("### 🎨 Pasatiempos e Intereses")
    st.markdown("""
- 🎧 Escuchar música  
- 🎬 Ver películas  
- 📖 Leer y escribir
    """)

    # Contacto
    st.markdown("### 📫 Contacto")
    st.markdown("📧 Correo: m.caso@pucp.edu.pe")  
    st.markdown("[📸 Instagram: @miguecaso](https://instagram.com/miguecaso)")

    # Cierre
    st.markdown("<br><p style='text-align:center; color:#6d597a;'>Gracias por visitar mi portafolio 🎶</p>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
