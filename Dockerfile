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

# Copy startup script and set permissions (as root)
COPY hworld/webapp/start.sh /app/start.sh
RUN chmod +x /app/start.sh && \
    chown hworld:hworld /app/start.sh

# Create data directory for persistence
RUN mkdir -p /data && chown hworld:hworld /data

# Switch to non-root user
USER hworld

# Expose server port
EXPOSE 28080

# Expose webapp port
EXPOSE 8080

# Set data directory
WORKDIR /data

# Run both server and webapp
CMD ["/app/start.sh"]
