# Use a small, modern Python base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only dependency file to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY assignments/fastapi-rest-apis /app/assignments/fastapi-rest-apis

# Expose port
EXPOSE 8000

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "assignments.fastapi-rest-apis.starter-code:app", "--host", "0.0.0.0", "--port", "8000"]
