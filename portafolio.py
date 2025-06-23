import streamlit as st

# Configurar la página
st.set_page_config(page_title="Portafolio de Miguel Caso", page_icon="🎤")

# Título
st.title("🎤 Portafolio de Miguel Caso")

# Separador
st.markdown("---")

# Sobre mí
st.header("👤 Sobre mí")
st.write("""
Soy una persona apasionada por el arte y la creatividad.  
Me gusta cantar, componer canciones, inventar historias y tocar instrumentos musicales.  
Creo que el esfuerzo es la clave para crecer. Siempre doy lo mejor de mí para cumplir mis metas.
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
Cortometraje que realicé con amigos. Trata sobre cómo el miedo puede afectar las relaciones.  
Es una historia emocional sobre lo que no se dice y lo que se siente.
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
