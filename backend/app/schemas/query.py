from pydantic import BaseModel
from typing import List

# شكل الطلب اللي هيجي من الـ Frontend
class QueryRequest(BaseModel):
    question: str

# شكل الإجابة اللي هترجع للـ Frontend
class QueryResponse(BaseModel):
    answer: str
    sources: List[str]