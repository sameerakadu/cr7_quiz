# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and source code
COPY requirements.txt ./
COPY app.py ./
COPY ronaldo_quiz.py ./
COPY static ./static
COPY templates ./templates

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Render will provide
EXPOSE 5000

# Run the app with gunicorn, binding to the port provided by Render
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:${PORT}"]
