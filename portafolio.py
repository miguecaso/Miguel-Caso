import streamlit as st

# Fondo con imagen de galaxia
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1470&q=80');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    /* Contenedor para el contenido */
    .contenido {
        background-color: rgba(255, 255, 255, 0.85); /* fondo blanco translúcido */
        border-radius: 15px;
        padding: 2rem 2.5rem;
        max-width: 900px;
        margin: 3rem auto 3rem auto;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Configurar la página
st.set_page_config(page_title="Portafolio de Miguel Caso", page_icon="🎤")

# Abrir contenedor
st.markdown("<div class='contenido'>", unsafe_allow_html=True)

# Aquí va todo tu contenido normal

# Título
st.title("🎤 Portafolio de Miguel Caso")

# Separador
st.markdown("---")

# Sobre mí
st.header("👤 Sobre mí")
st.write("""
Soy una persona apasionada por el arte y la creatividad. Me encanta cantar, componer canciones, inventar historias y expresarme a través de los instrumentos musicales.   Encuentro en la música y la narrativa una forma de conectar con los demás y conmigo mismo. Creo firmemente en el esfuerzo como clave del crecimiento personal; para mí, no hay victoria sin sacrificio. Cada meta que me propongo la enfrento con disciplina, entrega y corazón, porque sé que los sueños solo se alcanzan cuando se trabaja por ellos con constancia y pasión.
        """)

# Habilidades
st.header("🎯 Habilidades")
st.write("""
- Conocimientos en computación  
- Conocimientos audiovisuales  
- Limpieza de espacios  
- Aprendo rápido diferentes actividades
""")

# Perfil personal
st.header("🧩 Perfil personal")
st.write("""
- Estudiante de Comunicación Audiovisual  
- Amigable y responsable  
- Aprendo con facilidad  
- Me esfuerzo en todo lo que hago
""")

# Experiencia laboral
st.header("💼 Experiencia laboral")
st.write("""
- Cobrador de pasajes en Empresa ECO  
- Recojo y envío de encomiendas  
- Limpieza de buses interprovinciales  
- Producción de entrevistas  
- Cineplanet: atención al cliente, limpieza de salas y dulcería  
- Restaurante: limpieza, mozo, cocina y delivery
""")

# Proyecto
st.header("🎬 Proyecto: Entre Palabras")
st.write("""
**Entre Palabras** es un cortometraje escénico realizado en colaboración con un grupo de amigos, que aborda la falta de valentía que puede surgir cuando alguien cree haber encontrado el amor. A través de una narrativa íntima y emocional, exploramos cómo el miedo a expresarse y la inseguridad pueden transformar lo que parecía una conexión sincera en un vacío profundo, cubierto por la soledad.  
Esta historia refleja cómo, entre palabras no dichas y sentimientos reprimidos, se desdibuja la posibilidad de un verdadero encuentro emocional.
    """)

# Pasatiempos
st.header("🎨 Pasatiempos e intereses")
st.write("""
- Escuchar música  
- Ver películas  
- Leer y escribir
""")

# Contacto
st.header("📫 Contacto")
st.write("Correo: m.caso@pucp.edu.pe")  
st.write("Instagram: [@miguecaso](https://instagram.com/miguecaso)")

# Cierre
st.markdown("---")
st.write("Gracias por visitar mi portafolio 🎶")

# Cerrar contenedor
st.markdown("</div>", unsafe_allow_html=True)
