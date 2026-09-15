from fastapi import APIRouter, HTTPException
from app.schemas.query import QueryRequest, QueryResponse
from app.services.generation import generate_rag_response

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok", "message": "API is healthy and running!"}

@router.post("/query", response_model=QueryResponse)
def query_documents(request: QueryRequest):
    try:
        answer, sources = generate_rag_response(request.question)
        return QueryResponse(answer=answer, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))