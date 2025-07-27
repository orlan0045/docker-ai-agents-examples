# Use Python 3.11 slim image as base
FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1

# Install uv package manager
RUN pip install uv

WORKDIR /app

# Copy dependencies and install
COPY requirements.txt ./
RUN uv pip install --system -r requirements.txt

# Copy application code
COPY . .
RUN python -m compileall -q .

# Expose port for web interface
EXPOSE 8080

# Create entrypoint script
COPY <<EOF /entrypoint.sh
#!/bin/sh
set -e

echo "Using Docker Model Runner with \${MODEL_RUNNER_MODEL}"
export OPENAI_BASE_URL=\${MODEL_RUNNER_URL}
export OPENAI_MODEL_NAME=openai/\${MODEL_RUNNER_MODEL}
export OPENAI_API_KEY=cannot_be_empty

exec adk web --host 0.0.0.0 --port 8080 --log_level DEBUG
EOF
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]