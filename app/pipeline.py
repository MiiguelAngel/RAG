import os
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.logger import setup_logger
from app.config import PDF_PATH, INDEX_DIR, CHUNK_SIZE, CHUNK_OVERLAP

logger = setup_logger("pipeline", "pipeline.log")

def cargar_pdf(ruta_pdf: str) -> List[str]:
    """Carga y retorna el contenido del PDF"""
    logger.info(f"Cargando PDF desde: {ruta_pdf}")
    cargador = PyPDFLoader(ruta_pdf)
    paginas = cargador.load()
    logger.info(f"Documento cargado con {len(paginas)} páginas.")
    return paginas

def dividir_documentos(documentos: List[str]):
    """Divide el documento en fragmentos más pequeños"""
    logger.info("Dividiendo documento en fragmentos...")
    divisor = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    docs = divisor.split_documents(documentos)
    logger.info(f"Documento dividido en {len(docs)} fragmentos.")
    return docs

def indexar_y_embebed(docs: List[str], ruta_guardado: str = INDEX_DIR):
    """Genera embeddings y crea el índice FAISS"""
    logger.info("Generando embeddings y creando índice FAISS...")
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(ruta_guardado)
    logger.info(f"Índice FAISS guardado en {ruta_guardado}")
    return vectorstore

def cargar_o_crear_vectorstore(ruta_pdf=PDF_PATH, directorio_indice=INDEX_DIR):
    """Carga el vectorstore existente o crea uno nuevo"""
    if os.path.exists(directorio_indice):
        logger.info(f"Cargando índice FAISS desde: {directorio_indice}")
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.load_local(directorio_indice, embeddings, allow_dangerous_deserialization=True)
    else:
        paginas = cargar_pdf(ruta_pdf)
        docs = dividir_documentos(paginas)
        vectorstore = indexar_y_embebed(docs, directorio_indice)
    return vectorstore
