# Asistente RAG - Insurance 2030

Este proyecto implementa un sistema de Retrieval Augmented Generation (RAG) para el documento "Insurance 2030", utilizando tecnologías de procesamiento de lenguaje natural y bases de datos vectoriales para proporcionar respuestas precisas a preguntas sobre el contenido del documento.

## 🚀 Características Principales

### 1. Sistema de Autenticación
- Implementación de un sistema de autenticación basado en contraseña
- Protección de rutas y funcionalidades sensibles
- Interfaz de usuario intuitiva para el inicio de sesión

### 2. Procesamiento de Documentos
- Carga y procesamiento de documentos PDF
- División inteligente del texto en fragmentos (chunks)
- Generación de embeddings utilizando el modelo OpenAI
- Almacenamiento eficiente en base de datos vectorial FAISS

### 3. Sistema de Preguntas y Respuestas
- Interfaz interactiva para realizar preguntas
- Generación de respuestas contextuales basadas en el documento
- Sistema de calificación de respuestas (1-5 estrellas)
- Prevención de preguntas duplicadas
- Botón para generar nuevas preguntas

### 4. Seguimiento de Métricas
- Registro de interacciones de usuario
- Seguimiento de calificaciones promedio
- Estadísticas de uso del sistema
- Visualización de métricas en tiempo real

### 5. Interfaz de Usuario
- Diseño moderno y responsivo con Streamlit
- Tema personalizado con colores corporativos
- Barra lateral con información relevante
- Indicadores visuales de estado y progreso

## 🛠️ Herramientas Implementadas

### 1. Herramientas de Procesamiento de Texto
- **PyPDFLoader**: Para la carga y extracción de contenido de documentos PDF
- **RecursiveCharacterTextSplitter**: Para la división inteligente del texto en fragmentos manejables
- **OpenAIEmbeddings**: Para la generación de embeddings de alta calidad

### 2. Herramientas de Base de Datos Vectorial
- **FAISS (Facebook AI Similarity Search)**: Para el almacenamiento y búsqueda eficiente de vectores
- **VectorStore**: Para la gestión de almacenamiento vectorial
- **Indexación Automática**: Para la creación y actualización de índices

### 3. Herramientas de Modelado de Lenguaje
- **LangChain**: Para la construcción de cadenas de procesamiento de lenguaje natural
- **OpenAI GPT**: Para la generación de respuestas contextuales
- **Sentence Transformers**: Para la generación de embeddings de texto

### 4. Herramientas de Interfaz de Usuario
- **Streamlit**: Para la creación de la interfaz web interactiva
- **PIL (Python Imaging Library)**: Para el manejo de imágenes y logos
- **HTML/CSS Personalizado**: Para el diseño y estilizado de la interfaz

### 5. Herramientas de Seguimiento y Monitoreo
- **Sistema de Logging**: Para el registro de eventos y errores
- **Métricas Personalizadas**: Para el seguimiento de interacciones y calificaciones
- **Persistencia de Datos**: Para el almacenamiento de métricas y estadísticas

### 6. Herramientas de Seguridad
- **python-dotenv**: Para la gestión segura de variables de entorno
- **Sistema de Autenticación**: Para la protección de rutas y funcionalidades
- **Validación de Entradas**: Para la seguridad en el procesamiento de datos

### 7. Herramientas de Desarrollo
- **Git**: Para el control de versiones
- **Python Virtual Environment**: Para la gestión de dependencias
- **Pip**: Para la instalación y gestión de paquetes

## 🛠️ Arquitectura del Sistema

### Componentes Principales

1. **Pipeline de Procesamiento** (`app/pipeline.py`)
   - Carga de documentos PDF
   - División de texto en chunks
   - Generación de embeddings
   - Gestión de índice FAISS

2. **Cadena de QA** (`app/qa_chain.py`)
   - Construcción de la cadena de preguntas y respuestas
   - Integración con el modelo de lenguaje
   - Recuperación de contexto relevante

3. **Sistema de Métricas** (`app/metrics.py`)
   - Seguimiento de interacciones
   - Cálculo de estadísticas
   - Persistencia de datos

4. **Interfaz de Usuario** (`interface/streamlit_app.py`)
   - Gestión de sesiones
   - Interfaz de usuario
   - Visualización de resultados

### Flujo de Trabajo

1. **Inicialización**
   - Carga del documento PDF
   - Creación/actualización del índice FAISS
   - Inicialización de la cadena de QA

2. **Proceso de Pregunta**
   - Recepción de la pregunta del usuario
   - Recuperación de contexto relevante
   - Generación de respuesta
   - Presentación al usuario

3. **Feedback y Métricas**
   - Calificación de la respuesta
   - Registro de interacción
   - Actualización de estadísticas

## 🔧 Requisitos del Sistema

- Python 3.8+
- Dependencias principales:
  - langchain
  - streamlit
  - faiss-cpu
  - sentence-transformers
  - python-dotenv
  - openai

## 📦 Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd RAG
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
```bash
cp .env.example .env
# Editar .env con tus credenciales
```

## 🚀 Uso

1. Iniciar la aplicación:
```bash
streamlit run interface/streamlit_app.py
```

2. Acceder a la interfaz web:
   - Abrir navegador en `http://localhost:8501`
   - Ingresar credenciales de acceso

3. Interactuar con el sistema:
   - Realizar preguntas sobre el documento
   - Calificar respuestas
   - Consultar métricas en la barra lateral

## 📊 Métricas y Monitoreo

El sistema mantiene un registro detallado de:
- Total de interacciones
- Calificación promedio de respuestas
- Número de interacciones calificadas
- Tiempo de respuesta promedio del modelo
- Historial de tiempos de respuesta
- Timestamps precisos de preguntas y respuestas
- Uso de recursos

Las métricas se almacenan en formato JSON y se actualizan en tiempo real, permitiendo:
- Seguimiento del rendimiento del modelo
- Análisis de patrones de uso
- Identificación de cuellos de botella
- Optimización del tiempo de respuesta
- Análisis temporal de interacciones
- Seguimiento de latencia del sistema

Cada interacción registra:
- Timestamp exacto de la pregunta
- Timestamp exacto de la respuesta
- Tiempo de procesamiento
- Calificación del usuario
- Contenido completo de la interacción

## 🔒 Seguridad

- Autenticación basada en contraseña
- Protección de rutas sensibles
- Manejo seguro de credenciales
- Validación de entradas de usuario

## 🧪 Pruebas

El sistema incluye pruebas unitarias para:
- Procesamiento de documentos
- Generación de embeddings
- Sistema de QA
- Métricas y seguimiento

## 📝 Notas Adicionales

- El sistema requiere una conexión a internet para acceder a los modelos de OpenAI
- Se recomienda mantener actualizadas las dependencias
- El índice FAISS se regenera automáticamente si se detectan cambios en el documento

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, seguir las guías de contribución del proyecto.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.