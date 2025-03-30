import os
from dotenv import load_dotenv

load_dotenv()

PDF_PATH = "data/1210-Insurance-2030.pdf"
INDEX_DIR = "data/faiss_index"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME = "gpt-3.5-turbo"
OPENAI_TEMPERATURE = 0

TOP_K_RESULTS = 4