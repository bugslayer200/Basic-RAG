# Delivery Management System - Layered Architecture

## Architecture Overview

The system is organized into distinct layers, each with specific responsibilities, following a cloud-native architecture pattern.

---

## Architecture Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    USER LAYER                               │
│                      👤 End Users                            │
└──────────────────────────┬──────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              PRESENTATION LAYER                             │
│         🌐 Streamlit Web Interface                          │
│    • Chat Interface  • Document Upload  • Admin Panel      │
└──────────────────────────┬──────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  AGENT LAYER                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Current: Query Processing & Orchestration           │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Future: Multi-Agent System                           │  │
│  │  • Planner • Disambiguation • RAG • SQL • Compiler    │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│         KNOWLEDGE & CONTEXT LAYER                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  📚 Knowledge Base                                   │  │
│  │  • Document Parsing  • Text Extraction              │  │
│  │  • Chunking          • Metadata Management          │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  🧠 Context Management                               │  │
│  │  • Embedding Generation  • Vector Search            │  │
│  │  • Context Retrieval    • Relevance Scoring        │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│           CORE FOUNDATION LAYER                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  💾 Data Storage                                      │  │
│  │  • Vector Database (Qdrant)                          │  │
│  │  • Structured Database (Future)                       │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  🤖 AI/ML Services                                   │  │
│  │  • Embedding Models  • LLM Service                   │  │
│  │  • Prompt Management (Future)                         │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  🔐 Security & Authentication                        │  │
│  │  • SSO/OAuth2  • Token Management                    │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  CLOUD SERVICES                            │
│  ☁️ Qdrant Cloud  •  Groq Cloud  •  SharePoint Online      │
└─────────────────────────────────────────────────────────────┘
```

---

## Layer 1: Agent Layer

### Current Implementation ✅
- **Query Processing Handler**
  - Receives user queries
  - Coordinates search and retrieval
  - Manages response generation

### Future Implementation 🔮
- **Planner Agent (Orchestrator)**
  - Analyzes query intent
  - Routes to specialized agents
  - Coordinates multi-agent workflows

- **Disambiguation Agent**
  - Clarifies ambiguous queries
  - Multi-turn conversation handling

- **RAG Agent**
  - Specialized in retrieval
  - Vector search optimization

- **SQL Query Agent**
  - Generates database queries
  - Structured data access

- **Response Compiler Agent**
  - Synthesizes multi-source responses
  - Adds citations and sources

---

## Layer 2: Knowledge & Context Layer

### Knowledge Base Component
- **Document Processing**
  - Multi-format parsing (PDF, Word, PPT, TXT)
  - Text extraction and cleaning
  - Metadata extraction

- **Chunking Strategy**
  - Fixed-size chunking (500 chars)
  - Overlap management (100 chars)
  - Future: Semantic chunking

### Context Management Component
- **Embedding Generation**
  - Sentence Transformer models
  - Vector creation (384 dimensions)
  - Batch processing

- **Vector Search**
  - Similarity computation
  - Top-K retrieval
  - Relevance ranking

- **Context Retrieval**
  - Chunk aggregation
  - Context preparation for LLM
  - Relevance scoring

---

## Layer 3: Core Foundation Layer

### Data Storage
- **Vector Database (Qdrant)**
  - Embedding storage
  - Similarity search
  - Collection management
  - Cloud-hosted

- **Structured Database (Future)**
  - Metadata storage
  - Document relationships
  - User interactions

### AI/ML Services
- **Embedding Models**
  - Sentence Transformers
  - Model versioning
  - Performance optimization

- **LLM Service (Groq)**
  - Answer generation
  - Streaming responses
  - Token management

- **Prompt Management (Future)**
  - Langfuse integration
  - Version control
  - A/B testing

### Security & Authentication
- **SharePoint SSO/OAuth2**
  - Device code flow
  - Token management
  - Session handling

- **Access Control (Future)**
  - Role-based access
  - Permission management
  - Audit logging

---

## Layer 4: Cloud Services

### Cloud Infrastructure
- **Qdrant Cloud**
  - Managed vector database
  - Auto-scaling
  - High availability

- **Groq Cloud**
  - LLM inference service
  - High-performance processing
  - Global availability

- **SharePoint Online**
  - Enterprise document source
  - SSO integration
  - Secure access

- **Streamlit Cloud (Optional)**
  - Application hosting
  - Auto-deployment
  - Monitoring

---

## Data Flow Across Layers

### Document Upload Flow
```
User → Presentation → Agent → Knowledge Base → Foundation → Cloud
```

### Query Processing Flow
```
User → Presentation → Agent → Context Management → Foundation → Cloud → Response
```

### Future Agentic Flow
```
User → Presentation → Planner Agent → Specialized Agents → Tools → Foundation → Response
```

---

## Technology Stack by Layer

| Layer | Component | Technology | Status |
|-------|-----------|-----------|--------|
| **Agent** | Query Handler | Custom Python | ✅ |
| **Agent** | Multi-Agent | LangChain/LlamaIndex | 🔮 |
| **Knowledge** | Document Parser | pypdf, python-docx, python-pptx | ✅ |
| **Knowledge** | Embedding | Sentence Transformers | ✅ |
| **Foundation** | Vector DB | Qdrant Cloud | ✅ |
| **Foundation** | LLM | Groq API | ✅ |
| **Foundation** | Auth | MSAL (OAuth2) | ✅ |
| **Cloud** | Infrastructure | Qdrant, Groq, SharePoint | ✅ |

---

## Key Capabilities by Layer

### Agent Layer
- Intelligent query routing
- Multi-agent coordination
- Response synthesis

### Knowledge & Context Layer
- Document understanding
- Semantic search
- Context enrichment

### Core Foundation Layer
- Scalable storage
- AI/ML services
- Enterprise security

### Cloud Services
- Managed infrastructure
- Global availability
- Auto-scaling

