from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.api.routes import query
from app.services.retrieval import load_vector_store

# الدالة دي بتشتغل مرة واحدة بس أول ما السيرفر يقوم عشان تحمل قاعدة البيانات
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up: Loading vector store...")
    load_vector_store()
    yield
    print("Shutting down...")

app = FastAPI(title="Zoom FAQ RAG Assistant", lifespan=lifespan)

# السماح للـ Frontend يكلم السيرفر بدون مشاكل (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query.router)