import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Mi Primera App - Interfaces Multimodales",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 3rem !important;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem !important;
        color: #2e86ab;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
    }
    .card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin-bottom: 1rem;
    }
    .success-box {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
    }
    .info-box {
        background-color: #d1ecf1;
        color: #0c5460;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #bee5eb;
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown('<h1 class="main-header">🚀 Mi Primera App</h1>', unsafe_allow_html=True)

# Sección de introducción
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="sub-header">💡 Bienvenido a mi aplicación</h2>', unsafe_allow_html=True)
st.write("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.success("✅ Fácilmente puedo realizar backend y frontend.")
st.markdown('</div>', unsafe_allow_html=True)

# Imagen
image = Image.open('Interfaces Mult2.png')
st.image(image, caption='Interfaces Multimodales - Tecnología del Futuro', use_column_width=True)

# Sección de entrada de texto
st.markdown('<h2 class="sub-header">✍️ Escribe algo</h2>', unsafe_allow_html=True)
texto = st.text_input('**Ingresa tu texto aquí:**', 'Este es mi texto', help="Puedes modificar este texto con lo que quieras")
if texto:
    st.markdown(f'<div class="info-box"><strong>Texto escrito:</strong> {texto}</div>', unsafe_allow_html=True)

# Columnas
st.markdown('<h2 class="sub-header">📊 Ahora usemos 2 Columnas</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('### 🎯 Primera Columna')
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    
    resp = st.checkbox('✅ Estoy de acuerdo', help="Marca esta casilla si estás de acuerdo")
    if resp:
        st.markdown('<div class="success-box">🎉 ¡Correcto! Estamos en la misma sintonía</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('### 🔍 Segunda Columna')
    st.write("Selecciona la modalidad principal de tu interfaz:")
    
    modo = st.radio(
        "**Modalidades disponibles:**",
        ('👁️ Visual', '🔊 Auditiva', '✋ Táctil'),
        help="Elige la modalidad que consideres más importante"
    )
    
    if 'Visual' in modo:
        st.info('👁️ **La vista es fundamental para tu interfaz** - Los elementos visuales son clave para la experiencia del usuario.')
    elif 'Auditiva' in modo:
        st.info('🔊 **La audición es fundamental para tu interfaz** - El sonido puede guiar y mejorar la interacción.')
    elif 'Táctil' in modo:
        st.info('✋ **El tacto es fundamental para tu interfaz** - La respuesta háptica crea una experiencia más inmersiva.')
    st.markdown('</div>', unsafe_allow_html=True)

# Sección de botones
st.markdown('<h2 class="sub-header">🎮 Uso de Botones</h2>', unsafe_allow_html=True)
col_btn1, col_btn2 = st.columns([1, 3])

with col_btn1:
    if st.button('🔄 Presiona el botón', type='primary', help="Haz clic para ver el mensaje"):
        st.balloons()
        st.success('¡Gracias por presionar el botón! 🎉')
    else:
        st.warning('No has presionado el botón aún...')

# Selectbox
st.markdown('<h2 class="sub-header">📋 Selectbox de Modalidades</h2>', unsafe_allow_html=True)
in_mod = st.selectbox(
    "**Selecciona la modalidad que deseas utilizar:**",
    ("🎵 Audio", "📹 Visual", "📳 Háptico"),
    index=1,
    help="Elige una modalidad para ver la acción correspondiente"
)

if "Audio" in in_mod:
    set_mod = "🔊 Reproducir audio"
elif "Visual" in in_mod:
    set_mod = "🎬 Reproducir video"
elif "Háptico" in in_mod:
    set_mod = "📳 Activar vibración"

st.markdown(f'<div class="card"><strong>Acción seleccionada:</strong> {set_mod}</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Panel de Configuración")
    st.markdown("---")
    
    st.markdown("### 🎛️ Configura la Modalidad")
    mod_radio = st.radio(
        "**Escoge la modalidad a usar:**",
        ("👁️ Visual", "🔊 Auditiva", "✋ Háptica"),
        index=0
    )
    
    st.markdown("---")
    st.markdown("### 📊 Información de la App")
    st.info("""
    **Características:**
    - Interfaz multimodal
    - Diseño responsive
    - Fácil de usar
    - Personalizable
    """)
    
    st.markdown("---")
    st.markdown("### ℹ️ Acerca de")
    st.caption("Desarrollado con Streamlit 🎈")
    st.caption("Versión 1.0 - Interfaces Multimodales")
