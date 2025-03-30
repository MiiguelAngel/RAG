from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_core.vectorstores import VectorStore
from app.logger import setup_logger
from app.config import OPENAI_MODEL_NAME, OPENAI_TEMPERATURE, TOP_K_RESULTS

logger = setup_logger("qa_chain", "qa_chain.log")

def construir_cadena_qa(vectorstore: VectorStore):
    """Construye y retorna la cadena de preguntas y respuestas"""
    logger.info(f"Inicializando modelo {OPENAI_MODEL_NAME} con temperatura {OPENAI_TEMPERATURE}.")
    recuperador = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K_RESULTS}
    )
    llm = ChatOpenAI(model_name=OPENAI_MODEL_NAME, temperature=OPENAI_TEMPERATURE)
    cadena = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=recuperador,
        return_source_documents=False
    )
    logger.info("Cadena de QA construida exitosamente.")
    return cadena
