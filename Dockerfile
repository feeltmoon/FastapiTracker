# Use official Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of our code into the container
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# Expose the port for FastAPI (8000) and Streamlit (8501 by default)
EXPOSE 8000
EXPOSE 8501

# Command to start both FastAPI and Streamlit
# Using `&&` to chain commands
CMD uvicorn backend.main:app --host 0.0.0.0 --port 8000 & \
    streamlit run frontend/streamlit_app.py --server.port 8501 --server.address 0.0.0.0
