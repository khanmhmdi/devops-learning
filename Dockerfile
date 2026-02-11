# 1. Use stable Python (NOT 3.14)
FROM python:3.14-slim

# 2. Prevent Python from buffering logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set work directory
WORKDIR /app

# 4. Install system dependencies (optional but safe)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy requirements first (Docker cache optimization)
COPY requirements.txt .

# 6. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copy application code
COPY app ./app

# 8. Expose FastAPI port
EXPOSE 8000

# 9. Run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
