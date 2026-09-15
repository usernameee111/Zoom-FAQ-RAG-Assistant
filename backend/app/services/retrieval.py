import chromadb
from chromadb.utils import embedding_functions

# متغير عام عشان نحمل قاعدة البيانات مرة واحدة بس
collection = None

def load_vector_store():
    global collection
    # المسار ده لأننا هنشغل السيرفر من جوه فولدر backend
    persist_directory = "./data/vector_store"
    chroma_client = chromadb.PersistentClient(path=persist_directory)
    
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    
    # هنا بنعمل get عشان القاعدة موجودة بالفعل
    collection = chroma_client.get_collection(
        name="zoom_faqs",
        embedding_function=sentence_transformer_ef
    )
    print("Vector store loaded successfully!")

def retrieve_context(query: str, n_results: int = 3):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    docs = results['documents'][0]
    sources = results['metadatas'][0]
    return docs, sources