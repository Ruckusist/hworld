#!/bin/bash
# scripts/docker-run.sh
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

set -e

# Create data directory if it doesn't exist
mkdir -p ./data

echo "Starting hworld-server..."

docker compose up -d

echo "Server started. Logs: docker compose logs -f"
echo "Stop: docker compose down"
