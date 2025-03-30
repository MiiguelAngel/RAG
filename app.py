from app.pipeline import load_or_create_vectorstore
from app.qa_chain import build_qa_chain

def main():
    print("\n🔍 Asistente RAG - Documento: Insurance 2030")
    vectorstore = load_or_create_vectorstore()
    qa_chain = build_qa_chain(vectorstore)

    while True:
        query = input("\n💬 Pregunta (o escribe 'salir'): ").strip()
        if query.lower() in ["salir", "exit", "quit"]:
            print("👋 Cerrando sesión. ¡Hasta pronto!")
            break
        if not query:
            continue

        print("🧠 Generando respuesta...")
        try:
            answer = qa_chain.run(query)
            print(f"\n✅ Respuesta: {answer}")
        except Exception as e:
            print(f"\n⚠️ Error: {str(e)}")

if __name__ == "__main__":
    main()