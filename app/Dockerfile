FROM python:3.11-slim

# Create non-root user and group
RUN useradd -m appuser

WORKDIR /app

# Copy deps and install as root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code and set ownership
COPY app.py .
RUN chown -R appuser /app

# Drop privileges
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
