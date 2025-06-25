import streamlit as st

# Fondo con imagen de cielo nocturno estrellado
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1518984561899-cf2dc182d98b?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGVzcGFjaW8lMjBuZWdyb3xlbnwwfHwwfHx8MA%3D%3D');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        background-color: #0b0c10;  /* color oscuro de respaldo */
    }
    </style>
""", unsafe_allow_html=True)

# Configurar la página
st.set_page_config(page_title="Portafolio de Miguel Caso")

# Título
st.title("Portafolio de Miguel Caso")

# Separador
st.markdown("---")

# Sobre mí
st.header("Sobre Mí")
st.write("""
Soy una persona apasionada por el arte y la creatividad. Me encanta cantar, componer canciones, inventar historias y expresarme a través de los instrumentos musicales.   Encuentro en la música y la narrativa una forma de conectar con los demás y conmigo mismo. Creo firmemente en el esfuerzo como clave del crecimiento personal; para mí, no hay victoria sin sacrificio. Cada meta que me propongo la enfrento con disciplina, entrega y corazón, porque sé que los sueños solo se alcanzan cuando se trabaja por ellos con constancia y pasión.
        """)

st.header("Algunas Fotos Mías")

col1, col2 = st.columns(4)

with col1:
    st.image("foto1.jpg", caption="Soledad", width=300)

with col2:
    st.image("foto2.jpg", caption="Noche", width=300)

with col3:
    st.image("foto3.jpg", caption="Cineplanet", width=300)

with col4:
    st.image("foto4.jpg", caption="Feliz", width=300)

# Video del proyecto
st.subheader("GYM")
st.video("video.mp4")
st.video("video1.mp4")

# Habilidades
st.header("Habilidades")
st.write("""
- Conocimientos en computación  
- Conocimientos audiovisuales  
- Limpieza de espacios  
- Aprendo rápido diferentes actividades
""")

# Perfil personal
st.header("Perfil Personal")
st.write("""
- Estudiante de Comunicación Audiovisual  
- Amigable y responsable  
- Aprendo con facilidad  
- Me esfuerzo en todo lo que hago
""")

# Experiencia laboral
st.header("Experiencia Laboral")
st.write("""
- Cobrador de pasajes en Empresa ECO  
- Recojo y envío de encomiendas  
- Limpieza de buses interprovinciales  
- Producción de entrevistas  
- Cineplanet: atención al cliente, limpieza de salas y dulcería  
- Restaurante: limpieza, mozo, cocina y delivery
""")

# Proyecto
st.header("Proyecto: Entre Palabras")
st.write("""
**Entre Palabras** es un cortometraje escénico realizado en colaboración con un grupo de amigos, que aborda la falta de valentía que puede surgir cuando alguien cree haber encontrado el amor. A través de una narrativa íntima y emocional, exploramos cómo el miedo a expresarse y la inseguridad pueden transformar lo que parecía una conexión sincera en un vacío profundo, cubierto por la soledad.  
Esta historia refleja cómo, entre palabras no dichas y sentimientos reprimidos, se desdibuja la posibilidad de un verdadero encuentro emocional.
    """)

# Pasatiempos
st.header("Pasatiempos e Intereses")
st.write("""
- Escuchar música  
- Ver películas  
- Leer y escribir
""")

# Contacto
st.header("Contacto")
st.write("Correo: m.caso@pucp.edu.pe")  
st.write("Instagram: [@miguecaso](https://instagram.com/miguecaso)")

# Cierre
st.markdown("---")
st.write("Gracias por visitar Mi Portafolio")
