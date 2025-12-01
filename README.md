# Delivery Management System

A modern RAG (Retrieval-Augmented Generation) application built with Streamlit that enables semantic search and Q&A over uploaded documents. The system uses Qdrant for vector storage, Groq for LLM-powered responses, and supports multiple document formats.

## Features

- 📄 **Multi-Format Document Support**: Upload and process PDF, Word (.docx), PowerPoint (.pptx), and Text (.txt) files
- 🔍 **Semantic Search**: Ask questions about your documents and get AI-powered answers
- 🧠 **Vector Embeddings**: Uses sentence-transformers for creating document embeddings
- 💾 **Vector Database**: Stores document chunks in Qdrant for fast similarity search
- 🤖 **AI Responses**: Powered by Groq's LLM for generating contextual answers
- 🎨 **Modern UI**: Beautiful Streamlit interface with gradient styling and intuitive design

## Architecture

```
User Upload → Text Extraction → Chunking → Embedding → Qdrant Storage
                                                              ↓
User Query → Embedding → Vector Search → Context Retrieval → LLM → Answer
```

## Prerequisites

- Python 3.10 or higher
- Windows Long Path Support enabled (for PyTorch installation)
- Qdrant Cloud account or local Qdrant instance
- Groq API key

## Installation

### 1. Clone the Repository

```bash
cd RAG-POC
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

**Note**: If you encounter Windows Long Path errors during PyTorch installation:
- Enable Windows Long Path Support (requires admin rights)
- Run PowerShell as Administrator:
  ```powershell
  New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
  ```
- Restart your computer
- Reinstall PyTorch: `python -m pip install torch --index-url https://download.pytorch.org/whl/cpu`

### 3. Configure Environment Variables

Create a `.env` file in the project root with the following variables:

```env
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
GROQ_API_KEY=your_groq_api_key
COLLECTION_NAME=pdf_chunks
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
MAX_SEARCH_RESULTS=5
```

## Running the Application

### Start the Streamlit App

```bash
python -m streamlit run app.py
```

The application will start and automatically open in your browser at `http://localhost:8501`

If the browser doesn't open automatically, navigate to:
```
http://localhost:8501
```

### Alternative: Run with Custom Port

```bash
python -m streamlit run app.py --server.port 8502
```

## Usage

### 1. Upload Documents

1. Navigate to the **"📤 Upload PDF"** tab
2. Click **"Choose a document file"** and select:
   - PDF files (.pdf)
   - Word documents (.docx, .doc)
   - PowerPoint presentations (.pptx, .ppt)
   - Text files (.txt)
3. Adjust chunk size and overlap if needed:
   - **Chunk Size**: Number of characters per chunk (default: 500)
   - **Overlap**: Characters overlapping between chunks (default: 100)
4. Click **"📤 Upload & Ingest"** to process and store the document

### 2. Search and Query

1. Navigate to the **"🔍 Search"** tab
2. Enter your question in the search box
3. Click **"🔍 Search"**
4. View the AI-generated answer based on your documents

### 3. Manage Collection

- Use the **"🗑️ Delete Collection"** button in the sidebar to remove all stored documents
- The collection will be automatically recreated when you upload new documents

## Project Structure

```
RAG-POC/
├── app.py                 # Main Streamlit application
├── main.py                # CLI query script
├── ingest.py              # Document ingestion script
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── cloudrun.yaml          # Cloud Run deployment config
├── templates/             # HTML templates (legacy)
│   └── index.html
└── README.md              # This file
```

## Dependencies

- **streamlit**: Web application framework
- **qdrant-client**: Vector database client
- **groq**: LLM API client
- **sentence-transformers**: Text embeddings
- **pypdf**: PDF text extraction
- **python-docx**: Word document processing
- **python-pptx**: PowerPoint processing
- **numpy**: Numerical operations
- **python-dotenv**: Environment variable management

## Configuration

### Chunk Size and Overlap

- **Chunk Size**: Determines how much text is in each vector. Larger chunks provide more context but may be less precise.
- **Overlap**: Ensures important information at chunk boundaries isn't lost. Recommended: 10-20% of chunk size.

### Models

- **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2` (384 dimensions)
- **LLM Model**: `openai/gpt-oss-20b` (via Groq)

## Troubleshooting

### PyTorch Installation Issues

If you see "DLL load failed" errors:
1. Ensure Windows Long Path Support is enabled
2. Reinstall PyTorch: `python -m pip install torch --index-url https://download.pytorch.org/whl/cpu`

### Collection Not Found Error

If you see "Collection doesn't exist" errors:
- The collection is automatically created when you upload your first document
- If issues persist, check your Qdrant connection settings

### Document Processing Errors

- **Legacy formats (.doc, .ppt)**: Convert to .docx or .pptx format
- **Empty documents**: Ensure the file contains extractable text
- **Large files**: Consider splitting very large documents

## Docker Deployment

Build and run with Docker:

```bash
docker build -t delivery-mgmt-system .
docker run -p 8501:8501 --env-file .env delivery-mgmt-system
```

## Cloud Deployment

The project includes `cloudrun.yaml` for Google Cloud Run deployment. Update the environment variables in the YAML file before deploying.

## License

This project is for internal use.

## Support

For issues or questions, please contact the development team.

