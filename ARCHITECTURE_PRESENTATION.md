# Delivery Management System - Architecture Overview

## System Architecture Diagram

### Visual Representation

The architecture is organized into distinct layers with clear separation between current implementation and future enhancements.

---

## Layer 1: User Interface Layer

### Current Components ✅
- **Streamlit Web Interface**
  - Chat frontend for querying documents
  - Document upload interface (file and URL)
  - Real-time search and response display
  
- **Admin Interface**
  - Configuration management
  - Collection management (delete, view settings)
  - System status monitoring

---

## Layer 2: Application Layer

### Current Components ✅
- **Document Upload Handler**
  - Multi-format support (PDF, Word, PowerPoint, Text)
  - URL-based upload with SharePoint integration
  - File validation and processing
  
- **Search Handler**
  - Query processing and embedding
  - Vector similarity search
  - Context preparation for LLM
  
- **Authentication Handler**
  - SharePoint SSO/OAuth2 authentication
  - Device code flow for secure login
  - Token management and refresh

### Future Components 🔮
- **Planner Agent (Orchestrator)**
  - Intelligent query routing
  - Multi-agent coordination
  - Workflow orchestration

- **Disambiguation Agent**
  - Intent clarification for ambiguous queries
  - Multi-turn conversation handling
  - Context-aware disambiguation

---

## Layer 3: Processing Layer

### Current Components ✅
- **Document Parser**
  - PDF text extraction (pypdf)
  - Word document processing (python-docx)
  - PowerPoint processing (python-pptx)
  - Plain text file handling
  
- **Text Chunker**
  - Fixed-size chunking (500 characters)
  - Overlap management (100 characters)
  - Sequential chunk generation
  
- **Embedder**
  - Sentence Transformer model (all-MiniLM-L6-v2)
  - 384-dimensional vectors
  - Cosine similarity for search

### Future Components 🔮
- **Multi-modal Parser**
  - Image extraction and OCR
  - Table structure recognition
  - Chart and graph processing
  
- **Advanced Chunker**
  - Semantic chunking based on content
  - Sentence boundary detection
  - Topic-aware segmentation

---

## Layer 4: AI/LLM Layer

### Current Components ✅
- **Groq LLM**
  - Model: gpt-oss-20b
  - Streaming response generation
  - Context-aware answer synthesis
  - Temperature: 0.2 for consistent responses

### Future Components 🔮
- **Response Compiler Agent**
  - Multi-source response synthesis
  - Confidence scoring
  - Citation and source attribution

---

## Layer 5: Data Storage Layer

### Current Components ✅
- **Qdrant Vector Store**
  - Vector similarity search
  - Metadata storage (text chunks)
  - Collection management
  - Cosine distance metric

### Future Components 🔮
- **Structured Database**
  - Metadata storage
  - Document relationships
  - User interaction logs
  - Analytics and reporting

---

## Layer 6: External Services

### Current Components ✅
- **SharePoint Online**
  - Document source integration
  - SSO authentication
  - Direct file download
  
- **Groq API**
  - LLM inference service
  - Streaming responses
  - Token management

### Future Components 🔮
- **SQL Query Executor**
  - Database connection management
  - Query execution and optimization
  - Result formatting

---

## Agentic Architecture (Future)

### Agent Ecosystem

1. **Planner Agent (Orchestrator)**
   - **Role**: Central coordinator for all queries
   - **Responsibilities**:
     - Analyze user intent
     - Route to appropriate agents
     - Coordinate multi-agent workflows
     - Manage conversation state

2. **Disambiguation Agent**
   - **Role**: Clarify ambiguous queries
   - **Responsibilities**:
     - Ask clarifying questions
     - Understand user intent
     - Refine queries before processing

3. **RAG Agent**
   - **Role**: Specialized retrieval expert
   - **Responsibilities**:
     - Vector similarity search
     - Context retrieval
     - Relevance scoring
     - Multi-query expansion

4. **SQL Query Generator Agent**
   - **Role**: Structured data access
   - **Responsibilities**:
     - Generate SQL queries
     - Validate query syntax
     - Handle database schema
     - Optimize query performance

5. **Response Compiler Agent**
   - **Role**: Synthesize final responses
   - **Responsibilities**:
     - Combine multiple sources
     - Rank and filter results
     - Format responses
     - Add citations

---

## Data Flow

### Current Flow: Document Upload
```
User Upload → Authentication → Parse → Chunk → Embed → VectorDB
```

### Current Flow: Query Processing
```
User Query → Embed → Vector Search → Retrieve Context → LLM → Answer
```

### Future Flow: Agentic Query Processing
```
User Query 
  → Planner Agent (route)
    → Disambiguation Agent (if needed)
    → RAG Agent (vector search)
    → SQL Agent (structured data)
  → Response Compiler (synthesize)
  → Final Answer
```

---

## Technology Stack

### Current Stack
| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| Vector DB | Qdrant |
| Embeddings | Sentence Transformers |
| LLM | Groq (gpt-oss-20b) |
| Authentication | MSAL (OAuth2) |
| Document Processing | pypdf, python-docx, python-pptx |

### Future Stack
| Component | Technology (Planned) |
|-----------|---------------------|
| Agent Framework | LangChain / LlamaIndex |
| Prompt Management | Langfuse |
| Structured DB | PostgreSQL / MySQL |
| Multi-modal | Vision Models (CLIP, etc.) |
| Advanced Chunking | Semantic segmentation models |

---

## Key Features

### ✅ Implemented
- Multi-format document support
- Vector-based semantic search
- AI-powered Q&A
- SharePoint integration with SSO
- URL-based document upload
- Real-time streaming responses
- Collection management

### 🔮 Planned
- Multi-agent orchestration
- Intent disambiguation
- Hybrid search (vector + SQL)
- Multi-modal document processing
- Advanced semantic chunking
- Prompt versioning and management
- Structured data integration
- Analytics and reporting

---

## Security & Authentication

### Current
- SharePoint OAuth2/SSO
- Secure token management
- Session-based authentication

### Future
- Role-based access control (RBAC)
- Audit logging
- Data encryption at rest
- API key management

---

## Scalability Considerations

### Current
- Stateless application design
- Cloud-based vector database
- API-based LLM service

### Future
- Horizontal scaling support
- Caching layer for frequent queries
- Load balancing
- Distributed processing

---

## Monitoring & Observability

### Current
- Basic error handling
- User feedback messages

### Future
- Langfuse integration for prompt tracking
- Performance metrics
- Query analytics
- User behavior tracking
- System health monitoring

---

## Presentation Notes

### Key Points to Highlight

1. **Current State**: Fully functional RAG system with document upload and semantic search
2. **Future Vision**: Agentic architecture with intelligent orchestration
3. **Scalability**: Cloud-native design ready for enterprise deployment
4. **Security**: Enterprise-grade authentication and authorization
5. **Extensibility**: Modular design allows easy addition of new agents and capabilities

### Visual Elements
- Use color coding: Blue (current), Yellow (future), Green (storage), Purple (external)
- Show data flow with arrows
- Highlight agent interactions
- Emphasize the evolution path from current to future state

