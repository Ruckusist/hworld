# Dockerfile for hworld server
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

FROM python:3.12-slim

# Create non-root user
RUN useradd -m -u 1000 hworld

# Set working directory
WORKDIR /app

# Copy project files
COPY vendor/deskapp /app/vendor/deskapp
COPY hworld /app/hworld
COPY pyproject.toml /app/

# Install dependencies
RUN pip install --no-cache-dir -e /app/vendor/deskapp && \
    pip install --no-cache-dir -e /app

# Create data directory for persistence
RUN mkdir -p /data && chown hworld:hworld /data

# Switch to non-root user
USER hworld

# Expose server port
EXPOSE 28080

# Set data directory
WORKDIR /data

# Run server
CMD ["python", "-m", "hworld.server"]
