# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first (for efficient caching)
COPY requirements.txt .

RUN apt-get update && apt-get install -y python3-opencv

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files
COPY main.py .

# Expose the port FastAPI runs on
EXPOSE 2000

# Run Uvicorn when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2000"]
