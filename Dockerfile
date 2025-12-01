# ============================
# Base Image
# ============================
FROM python:3.10-slim

# Avoid Python writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# ============================
# Install system dependencies
# ============================
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libglib2.0-dev \
    libgomp1 \
    git \
    && rm -rf /var/lib/apt/lists/*

# ============================
# Copy requirements (if you have one)
# ============================
COPY requirements.txt /app/requirements.txt

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# ================================
# PRE-DOWNLOAD SENTENCE TRANSFORMER MODEL
# ================================
RUN python - <<EOF
from sentence_transformers import SentenceTransformer
SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
EOF


# ============================
# Copy app code
# ============================
COPY . /app

# Expose cloud run default port (optional but good practice)
EXPOSE 8080

# Streamlit CMD with fallback port
CMD sh -c "streamlit run app.py --server.port=\${PORT:-8501} --server.address=0.0.0.0"

