```markdown
# 💬 Zoom FAQ RAG Assistant

## 👩‍💻 Done by

* **Shams Maher Goda**
* **Shrouk Mohammed Eissa**

## 📌 Overview
This project is a fully functional **Retrieval-Augmented Generation (RAG)** pipeline acting as a Customer Support Assistant for Zoom. It answers user queries strictly based on provided Zoom FAQ PDF documents, ensuring accurate, hallucination-free, and cited responses. This fulfills the **Core Track** requirements.

## 🏗️ Architecture Diagram
```text
User Input 
   │
   ▼
[ Streamlit Frontend ] ──(REST API)──> [ FastAPI Backend ]
                                              │
                                              ├── 1. Embed Query (all-MiniLM-L6-v2)
                                              ├── 2. Retrieve Context (ChromaDB)
                                              └── 3. Generate Answer (Ollama - llama3.2:1b)
                                              │
[ Display Answer & Citations ] <──(JSON)──────┘

```

## 🛠️ Tech Stack

* **LLM Engine:** Local `llama3.2:1b` (via Ollama)
* **Vector Store & Embeddings:** ChromaDB & `sentence-transformers` (`all-MiniLM-L6-v2`)
* **Backend:** Python, FastAPI, Pydantic, Uvicorn
* **Frontend:** Streamlit
* **Data Processing:** PyPDF2, NLTK, LangChain concepts

## 📁 Project Structure

```text
rag-assistant-project/
├── backend/
│   ├── app/                # FastAPI application (main, routes, schemas, services)
│   ├── data/               # Persisted ChromaDB vector store & config.json
│   ├── tests/              # Pytest files (test_main.py)
│   ├── .env.example
│   └── requirements.txt
├── frontend/
│   ├── app.py              # Streamlit Chat Interface
│   ├── api_client.py       # Backend API wrapper
│   ├── .env.example
│   └── requirements.txt
├── notebooks/
│   └── rag_pipeline.ipynb  # Complete data pipeline & evaluation (Phases 1, 2)
├── data/                   # Original Zoom FAQ PDFs
├── .gitignore
└── README.md

```

## 📊 Domain & Data Description

The domain focuses on **Zoom Customer Support**. The dataset consists of 3 PDF documents detailing FAQ policies regarding Zoom Accounts, Large Meetings, Video Webinars, pricing, and system requirements. The corpus was cleaned and split into 48 overlapping chunks (500 chars limit, 50 overlap).

## ⚙️ Setup Instructions

### 1. Backend Setup

```bash
cd backend
python -m venv .venv
# Activate virtual environment
pip install -r requirements.txt
python -m uvicorn app.main:app --reload

```

*API runs at `http://localhost:8000/docs*`

### 2. Frontend Setup (New Terminal)

```bash
cd frontend
# Activate virtual environment
pip install -r requirements.txt
python -m streamlit run app.py

```

## 🔐 Environment Variables

| Component | Variable | Example Value | Description |
| --- | --- | --- | --- |
| Backend | `HOST` | `0.0.0.0` | API Host address |
| Backend | `PORT` | `8000` | API Port |
| Frontend | `API_BASE_URL` | `http://127.0.0.1:8000` | URL to connect to the FastAPI backend |

## 📡 API Reference

**Endpoint:** `POST /query`
**cURL Example:**

```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/query](http://127.0.0.1:8000/query)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"question": "Do I need an account to use Zoom?"}'

```

## 📈 Evaluation Results (Phase 2.6)

The pipeline was evaluated on 10 diverse questions. Below is a sample of the results demonstrating the model's accuracy and strict adherence to context (refusal to hallucinate):

| Question | Retrieved Source | Answer Grounding | Correct? |
| --- | --- | --- | --- |
| How many video panelists are allowed in a Zoom Video Webinar? | zoom-video-webinars-faq.pdf | "You can have up to 100 video panelists..." | Yes |
| Do I need an account to use Zoom? | ZoomFAQ.pdf | "You do not need a Zoom account..." | Yes |
| Is the Zoom link HIPAA compliant? | Zoom-FAQs.pdf | "I don't have enough information to answer that." | Yes (No Hallucination) |

## 📸 Application Screenshots

![Grounded Answer Demo](screenshots/answer1.png)

![Anti-Hallucination Demo](screenshots/answer2.png)

```