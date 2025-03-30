import streamlit as st
import sys
import os
from PIL import Image

# Añadir el directorio raíz al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.pipeline import cargar_o_crear_vectorstore
from app.qa_chain import construir_cadena_qa
from app.metrics import SeguimientoMetricas
from dotenv import load_dotenv

load_dotenv()

# Configuración de la página
st.set_page_config(page_title="RAG - Seguros Bolívar", layout="centered")

# Inicializar el tracker de métricas
seguimiento_metricas = SeguimientoMetricas()

# Inicializar el estado de la sesión
if 'query' not in st.session_state:
    st.session_state.query = ""
if 'answer' not in st.session_state:
    st.session_state.answer = None
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'rated' not in st.session_state:
    st.session_state.rated = False
if 'qa_chain' not in st.session_state:
    st.session_state.qa_chain = None

# Función para verificar la contraseña
def check_password():
    """Retorna `True` si el usuario tiene la contraseña correcta."""

    def password_entered():
        """Verifica si la contraseña ingresada es correcta."""
        if st.session_state["username"] == os.getenv("STREAMLIT_USERNAME"):
            if st.session_state["password"] == os.getenv("STREAMLIT_PASSWORD"):
                st.session_state["password_correct"] = True
                del st.session_state["password"]  # No mostrar la contraseña.
            else:
                st.session_state["password_correct"] = False

    # Retorna `True` si la contraseña es validada.
    if st.session_state.get("password_correct", False):
        return True

    # Muestra el formulario de inicio de sesión.
    st.markdown(
        """
        <div style="background-color: #FFFFFF; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h2 style="color: #006228; text-align: center; margin-bottom: 20px;">🔐 Inicio de Sesión</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.text_input("Usuario", on_change=password_entered, key="username")
    st.text_input("Contraseña", type="password", on_change=password_entered, key="password")
    if "password_correct" in st.session_state:
        st.error("😕 Usuario o contraseña incorrectos")
    return False

# Verificar la contraseña antes de mostrar la aplicación
if not check_password():
    st.stop()

# Logo e identidad visual
col1, col2 = st.columns([2, 1])
with col2:
    logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "logo-seguros-bolivar.png")
    logo = Image.open(logo_path)
    st.image(logo, width=150)

with col1:
    st.title("Asistente Inteligente - Insurance")

# Mostrar métricas actuales
metrics = seguimiento_metricas.obtener_metricas()
st.sidebar.markdown("### 📊 Métricas del Modelo")
st.sidebar.markdown(f"**Total de Interacciones:** {metrics['total_interactions']}")
st.sidebar.markdown(f"**Calificación Promedio:** {metrics['average_rating']:.1f}/5")
st.sidebar.markdown(f"**Interacciones Calificadas:** {metrics['rated_interactions']}")

# Campo de pregunta con estilo mejorado
st.markdown(
    """
    <div style="background-color: #FFFFFF; padding: 5px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h4 style="color: #006228; margin-bottom: 10px;">💬 Haz tu pregunta</h4>
    </div>
    """,
    unsafe_allow_html=True
)

# Campo de entrada y botón de enviar
col1, col2 = st.columns([4, 1])
with col1:
    query = st.text_area("", placeholder="Escribe tu pregunta aquí...", key="query_input", height=100)

with col2:
    st.markdown("<div style='height: 100px; display: flex; align-items: center;'>", unsafe_allow_html=True)
    if st.button("Enviar", type="primary"):
        if query:
            st.session_state.query = query
            st.session_state.show_answer = True
        else:
            st.warning("Por favor, escribe una pregunta")
    st.markdown("</div>", unsafe_allow_html=True)

# Botón para nueva pregunta
if st.session_state.show_answer:
    if st.button("🔄 Nueva Pregunta", type="secondary"):
        # Limpiar el estado
        st.session_state.query = ""
        st.session_state.answer = None
        st.session_state.show_answer = False
        st.session_state.rated = False
        st.session_state.qa_chain = None
        # Reiniciar la aplicación
        st.rerun()

# Procesar la pregunta solo cuando se presiona el botón
if st.session_state.show_answer:
    with st.spinner("🧠 Procesando tu pregunta..."):
        # Solo crear el qa_chain si no existe
        if st.session_state.qa_chain is None:
            vectorstore = cargar_o_crear_vectorstore()
            st.session_state.qa_chain = construir_cadena_qa(vectorstore)
        
        # Solo obtener la respuesta si no existe
        if st.session_state.answer is None:
            st.session_state.answer = st.session_state.qa_chain.run(st.session_state.query)

        st.markdown(
            f"""
            <div style="background-color: #FFFFFF; border-left: 5px solid #006228; padding: 15px; margin-top: 20px; border-radius: 5px;">
                <h4 style="color: #006228;">Respuesta:</h4>
                <p style="color: #333333;">{st.session_state.answer}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Sección de calificación
        if not st.session_state.rated:
            st.markdown("### 📝 Califica esta respuesta")
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                if st.button("1 ⭐"):
                    seguimiento_metricas.agregar_interaccion(st.session_state.query, st.session_state.answer, calificacion=1)
                    st.session_state.rated = True
                    st.success("¡Gracias por tu calificación!")
            with col2:
                if st.button("2 ⭐"):
                    seguimiento_metricas.agregar_interaccion(st.session_state.query, st.session_state.answer, calificacion=2)
                    st.session_state.rated = True
                    st.success("¡Gracias por tu calificación!")
            with col3:
                if st.button("3 ⭐"):
                    seguimiento_metricas.agregar_interaccion(st.session_state.query, st.session_state.answer, calificacion=3)
                    st.session_state.rated = True
                    st.success("¡Gracias por tu calificación!")
            with col4:
                if st.button("4 ⭐"):
                    seguimiento_metricas.agregar_interaccion(st.session_state.query, st.session_state.answer, calificacion=4)
                    st.session_state.rated = True
                    st.success("¡Gracias por tu calificación!")
            with col5:
                if st.button("5 ⭐"):
                    seguimiento_metricas.agregar_interaccion(st.session_state.query, st.session_state.answer, calificacion=5)
                    st.session_state.rated = True
                    st.success("¡Gracias por tu calificación!")
        else:
            st.markdown("### ✅ Respuesta calificada")