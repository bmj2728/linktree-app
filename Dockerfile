FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Create directories for mounted volumes
RUN mkdir -p /config /templates/default /templates/custom

# Copy default templates
COPY templates/default/ /templates/default/

# Set environment variables
ENV CONFIG_PATH=/config/config.yaml
ENV TEMPLATES_PATH=/templates
ENV AVATAR_PATH=/config/avatar.png

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
