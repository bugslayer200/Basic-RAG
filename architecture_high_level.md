# Delivery Management System - High-Level Architecture

## System Overview

A RAG (Retrieval-Augmented Generation) system for delivery management that enables semantic search and Q&A over organizational documents.

---

## High-Level Architecture with Cloud Layers

```
┌─────────────────────────────────────────────────────────────────────┐
│                         USER LAYER                                  │
│                            👤 Users                                  │
└────────────────────────────┬────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                               │
│              🌐 Web Interface (Streamlit)                           │
│         • Document Upload  • Search & Query                         │
└────────────────────┬────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    AGENT LAYER                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  🤝 Multi-Agent Orchestration (Future)                       │  │
│  │  • Planner Agent  • Disambiguation Agent                    │  │
│  │  • RAG Agent      • SQL Query Agent                        │  │
│  │  • Response Compiler Agent                                  │  │
│  └──────────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  🔍 Current: Query Processing                               │  │
│  │  • Query Handler  • Search Orchestration                    │  │
│  └──────────────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────────┐
│              KNOWLEDGE & CONTEXT LAYER                              │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  📚 Knowledge Base                                           │  │
│  │  • Document Processing  • Text Extraction                  │  │
│  │  • Chunking Strategy    • Metadata Management               │  │
│  └──────────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  🧠 Context Management                                       │  │
│  │  • Embedding Generation  • Vector Search                    │  │
│  │  • Context Retrieval    • Relevance Scoring                │  │
│  └──────────────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  CORE FOUNDATION LAYER                              │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  💾 Data Storage                                              │  │
│  │  • Vector Database (Qdrant)  • Structured Data (Future)     │  │
│  │  • Embedding Storage         • Metadata Store               │  │
│  └──────────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  🤖 AI/ML Services                                           │  │
│  │  • Embedding Models (Sentence Transformers)                 │  │
│  │  • LLM Service (Groq API)                                   │  │
│  │  • Prompt Management (Langfuse - Future)                     │  │
│  └──────────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  🔐 Security & Authentication                                │  │
│  │  • SharePoint SSO/OAuth2  • Token Management                 │  │
│  │  • Access Control (Future)                                   │  │
│  └──────────────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    CLOUD SERVICES                                   │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  ☁️ Cloud Infrastructure                                       │  │
│  │  • Qdrant Cloud (Vector DB)  • Groq Cloud (LLM)              │  │
│  │  • SharePoint Online        • Streamlit Cloud (Deployment)   │  │
│  └──────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Layer Breakdown

### 1. Agent Layer
**Purpose**: Intelligent orchestration and query processing

**Current Components:**
- Query Processing Handler
- Search Orchestration
- Response Generation

**Future Components:**
- **Planner Agent**: Routes queries to appropriate agents
- **Disambiguation Agent**: Clarifies user intent
- **RAG Agent**: Specialized retrieval expert
- **SQL Query Agent**: Structured data access
- **Response Compiler Agent**: Synthesizes final responses

---

### 2. Knowledge & Context Layer
**Purpose**: Document processing, knowledge extraction, and context management

**Components:**
- **Knowledge Base**
  - Document parsing (PDF, Word, PPT, TXT)
  - Text extraction and cleaning
  - Chunking strategies
  - Metadata extraction and management
  
- **Context Management**
  - Embedding generation
  - Vector similarity search
  - Context retrieval and ranking
  - Relevance scoring

---

### 3. Core Foundation Layer
**Purpose**: Core infrastructure, storage, and services

**Components:**
- **Data Storage**
  - Vector Database (Qdrant) - Current
  - Structured Database (Future)
  - Metadata storage
  - Document index management

- **AI/ML Services**
  - Embedding models (Sentence Transformers)
  - LLM service (Groq API)
  - Prompt management (Langfuse - Future)
  - Model versioning

- **Security & Authentication**
  - SharePoint SSO/OAuth2
  - Token management
  - Access control (Future)
  - Audit logging (Future)

---

### 4. Cloud Services
**Purpose**: Cloud-hosted infrastructure and services

**Services:**
- **Qdrant Cloud**: Vector database hosting
- **Groq Cloud**: LLM inference service
- **SharePoint Online**: Document source
- **Streamlit Cloud**: Application hosting (optional)

---

## Data Flow Across Layers

### Upload Flow
```
User → Presentation Layer → Agent Layer → Knowledge Layer → Foundation Layer → Cloud
```

### Query Flow
```
User → Presentation Layer → Agent Layer → Knowledge Layer → Foundation Layer → Cloud → Response
```

### Detailed Query Flow
```
1. User Query (Presentation Layer)
   ↓
2. Agent Layer: Process & Route Query
   ↓
3. Knowledge Layer: Generate Embedding & Search Context
   ↓
4. Foundation Layer: Vector Search in Qdrant
   ↓
5. Knowledge Layer: Retrieve & Rank Context
   ↓
6. Foundation Layer: LLM Service (Groq)
   ↓
7. Agent Layer: Compile Response
   ↓
8. Presentation Layer: Display Answer
```

---

## Technology Mapping by Layer

| Layer | Technology | Status |
|-------|-----------|--------|
| **Agent Layer** | Custom Logic (Future: LangChain/LlamaIndex) | 🔄 Partial |
| **Knowledge & Context** | Sentence Transformers, Custom Processing | ✅ Current |
| **Foundation - Storage** | Qdrant (Cloud) | ✅ Current |
| **Foundation - AI/ML** | Groq API, Sentence Transformers | ✅ Current |
| **Foundation - Security** | MSAL (OAuth2) | ✅ Current |
| **Cloud Services** | Qdrant Cloud, Groq Cloud, SharePoint Online | ✅ Current |

---

## Key Features by Layer

### Agent Layer
- ✅ Query processing and routing
- 🔮 Multi-agent orchestration
- 🔮 Intent disambiguation
- 🔮 Response synthesis

### Knowledge & Context Layer
- ✅ Multi-format document processing
- ✅ Semantic embedding generation
- ✅ Vector similarity search
- 🔮 Advanced chunking strategies
- 🔮 Multi-modal processing

### Core Foundation Layer
- ✅ Vector database storage
- ✅ LLM integration
- ✅ Authentication & security
- 🔮 Structured data storage
- 🔮 Prompt versioning

### Cloud Services
- ✅ Scalable vector database
- ✅ High-performance LLM
- ✅ Enterprise document source
- 🔮 Auto-scaling infrastructure
