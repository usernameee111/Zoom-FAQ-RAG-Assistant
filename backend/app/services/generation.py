import ollama
from app.services.retrieval import retrieve_context

def generate_rag_response(query: str):
    # 1. استرجاع النصوص والمصادر
    docs, sources = retrieve_context(query)
    
    # 2. تجهيز السياق والمصادر
    context = ""
    unique_sources = set()
    for i in range(len(docs)):
        context += f"[Source: {sources[i]['source']}]\n{docs[i]}\n\n"
        unique_sources.add(sources[i]['source'])
        
    # 3. بناء الـ Prompt
    prompt = f"""You are a customer support assistant for Zoom.
    Answer the user's question concisely using ONLY the provided context below.
    If the answer is not in the context, say "I don't have enough information to answer that."

    Context:
    {context}

    Question: {query}
    Answer:"""
    
    # 4. إرسال الطلب لنموذج Ollama
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    answer = response['message']['content']
    
    return answer, list(unique_sources)