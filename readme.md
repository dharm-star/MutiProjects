langchain-projects/
│
├── project_01_chatbot/
├── project_02_pdf_rag/
├── project_03_sql_agent/
├── project_04_tools_agent/
├── project_05_multi_agent/
---------------------------------------------------
genai-labs/

01-chat-model/

02-embeddings/

03-vector-store/

04-retriever/

05-prompts/

06-rag/

07-tool-calling/

08-mcp/

09-agents/

10-langgraph/
---------------------------------------------------
Our Product

AI Knowledge Assistant

Features will be added one by one

v1.0  ✅ Ask questions from PDF

v1.1  Persistent Vector DB

v1.2  Multiple PDFs

v1.3  Conversation History

v1.4  Source Citation

v1.5  Streaming

v1.6  Hybrid Search

v2.0  Tools

v2.1  MCP

v2.2  Agent

v3.0  LangGraph

---------------------------------------------------
APIs You Should Remember
ChatGoogleGenerativeAI

SystemMessage
HumanMessage
AIMessage

PromptTemplate
ChatPromptTemplate

PyPDFLoader

RecursiveCharacterTextSplitter

GoogleGenerativeAIEmbeddings

FAISS.from_documents()

vector_store.as_retriever()

RunnablePassthrough()

StrOutputParser()
-------------------------------------------
Phase 1 — LangChain Core ✅
✅ Chat Models
✅ Messages
✅ Prompt Templates
✅ ChatPromptTemplate
✅ Document Loader
✅ Text Splitter
✅ Embeddings
✅ Vector Store
✅ Retriever
✅ LCEL

----------------------------------------------
Knowledge Map

This is the map we'll complete.
LangChain

Models              ✅
Messages            ✅
Prompts             ✅
Documents           ✅
Splitters           ✅
Embeddings          ✅
Vector Stores       ✅
Retrievers          ✅
LCEL                ✅
Conversation        ⏳
Output Parsers      ⏳
Tools               ⏳
Tool Calling        ⏳
Memory              ⏳
MCP                 ⏳
Agents              ⏳
LangGraph           ⏳
Deployment          ⏳

-----------------------------------------
mini-rag/
│
├── data/
│   └── notes.pdf
│
├── rag/
│   ├── __init__.py
│   ├── config.py
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectordb.py
│   ├── retriever.py
│   ├── prompt.py
│   └── chain.py
│
├── ingest.py
├── chat.py
├── .env
├── pyproject.toml
└── uv.lock

-------------------------------------------
One more improvement

We're going to keep a knowledge map as we learn.

LangChain

├── Models
│
├── Prompts
│
├── Documents
│
├── Splitters
│
├── Embeddings
│
├── Vector Stores
│
├── Retrievers
│
├── LCEL
│
├── Memory
│
├── Tools
│
├── Agents
│
├── MCP
│
└── LangGraph

--------------------------------------------------
Optimized Roadmap (90% of Interview Questions)

| #     | Component                | Time   | Why                    |
| ----- | ------------------------ | ------ | ---------------------- |
| ✅ 1   | Chat Models              | 15 min | Done                   |
| ✅ 2   | Messages                 | 15 min | Done                   |
| ✅ 3   | Prompt Templates         | 20 min | Done                   |
| ✅ 4   | Document Loader          | 15 min | Done                   |
| ✅ 5   | Text Splitter            | 20 min | Done                   |
| ✅ 6   | Embeddings               | 30 min | Done                   |
| 🔜 7  | Vector Store + Retriever | 45 min | Core RAG               |
| 🔜 8  | LCEL (Runnable Pipeline) | 45 min | **Very important**     |
| 🔜 9  | Complete RAG Project     | 1 hr   | Connect everything     |
| 🔜 10 | Tools                    | 45 min | Interview favorite     |
| 🔜 11 | Tool Calling             | 30 min | LLM + Tools            |
| 🔜 12 | Agents                   | 1 hr   | Decision making        |
| 🔜 13 | MCP                      | 1 hr   | Modern architecture    |
| 🔜 14 | LangGraph                | 2 hr   | Advanced orchestration |

----------------------------------------------------------------------
This is the most important diagram in LangChain
                 Question
                     │
         ┌───────────┴───────────┐
         │                       │
         ▼                       ▼
Retriever               RunnablePassthrough
         │                       │
         ▼                       │
format_docs                     │
         │                       │
         └───────────┬───────────┘
                     ▼
              ChatPromptTemplate
                     │
                     ▼
                  Gemini
                     │
                     ▼
             StrOutputParser
                     │
                     ▼
                 Final Answer

-----------------------------------------------------------------------------
Instead of relying on one retriever:
            Question
               │
      ┌────────┴────────┐
      ▼                 ▼
   FAISS            BM25
(Semantic)       (Keyword)
      │                 │
      └────────┬────────┘
               ▼
        Merge Results
               ▼
             Gemini

----------------------------------------------------------------------------
Final Architecture
mini-rag/
│
├── api/
│   ├── __init__.py
│   └── routes.py
│
├── services/
│   ├── __init__.py
│   └── rag_service.py
│
├── repositories/
│   ├── __init__.py
│   ├── conversation_repository.py
│   └── message_repository.py
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── schema.py
│
├── rag/
│   ├── config.py
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectordb.py
│   ├── retriever.py
│   ├── prompt.py
│   └── chain.py
│
├── data/
│   ├── rag.db
│   └── faiss_index/
│
├── app.py
├── ingest.py
├── chat.py
├── schemas.py
└── requirements

-------------------------------------------------------------
Next Features (Production Priority)

Here's the roadmap I'd follow:

Priority	Feature	Status
✅	RAG Pipeline	Done
✅	FAISS Persistence	Done
✅	Multi-PDF	Done
✅	FastAPI	Done
⏭️	Streaming Responses	Next
⏭️	Conversation Memory	After Streaming
⏭️	Source Citation UI	After Memory
⏭️	Multi-user Conversations	Later
⏭️	Docker	Later
⏭️	Deployment	Later
⏭️	Evaluation (RAGAS)	Later
⏭️	Monitoring	Later

--------------------------------------------------
Question
   │
   ▼
Retrieve
   │
   ▼
Documents + Score
   │
   ▼
Confidence Check
   │
   ├──── NO
   │      │
   │      ▼
   │ Return "No relevant documents found."
   │
   ▼ YES
Format Context
   │
   ▼
Gemini

-----------------------------------------------------
What we've completed
Foundation
✅ FastAPI
✅ LangChain basics
✅ Gemini integration
✅ PDF loading
✅ Chunking
✅ Embeddings
✅ FAISS
✅ Prompt template
✅ RAG chain
Advanced RAG
✅ Conversation memory (SQLite)
✅ Streaming responses
✅ Hybrid Search (FAISS + BM25)
✅ Metadata Filtering
✅ Source citations
✅ Reranking (concept + integration)

This is already a strong RAG project.

What's next (recommended order)
Sprint 3.3 — Hallucination Reduction (Current)
⏳ Retrieval confidence score
⏳ Threshold checking
⏳ Better RAG prompt ("answer only from context")
⏳ Context validation
⏳ "I don't know" fallback

Goal: Make the chatbot refuse to answer when the evidence is weak.

Sprint 3.4 — Evaluation

Learn how to answer:

"How do you know your RAG is good?"

We'll cover:

Precision@K
Recall@K
Hit Rate
MRR (Mean Reciprocal Rank)
LLM-as-a-Judge
Basic evaluation datasets

This is what many candidates don't know.

Sprint 4 — Vector Databases

Right now you know FAISS.

We'll compare it with:

Chroma
Qdrant
SQLite Vector
FAISS

You'll understand when to choose each one.

Sprint 5 — Agents

We'll move beyond simple RAG.

Topics include:

LangGraph
Tool Calling
Web Search
SQL Agent
Multi-step reasoning
Memory inside agents
Sprint 6 — Fine-tuning

Only now do we move to:

LoRA
QLoRA
PEFT
Quantization
Fine-tuning open models

At this point you'll understand when fine-tuning is the right solution instead of RAG.

Sprint 7 — Production

We'll cover deployment topics such as:

Docker
Logging
Monitoring
Authentication
Rate limiting
Caching
Deployment