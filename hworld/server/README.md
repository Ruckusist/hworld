# Hworld Server
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

## Overview

Hworld server is a minimal implementation using the deskapp server
framework. It provides user authentication, pub/sub messaging, and
session management.

## Quick Start

### Local Development

```bash
# Install dependencies
pip install -e vendor/deskapp
pip install -e .

# Run server
python -m hworld.server

# Or use the command
hworld-server
```

### Docker

```bash
# Build
./scripts/docker-build.sh

# Run
./scripts/docker-run.sh

# Stop
docker-compose down
```

## Configuration

### Environment Variables

- `HWORLD_HOST`: Server host (default: 0.0.0.0)
- `HWORLD_PORT`: Server port (default: 28080)
- `HWORLD_BUFFER`: Buffer size (default: 1024)
- `HWORLD_VERBOSE`: Enable verbose logging (default: true)

### Config File

Copy `config.example.toml` to `config.toml` and edit as needed.

## Testing

```bash
# In one terminal
python -m hworld.server

# In another terminal
python examples/test_client.py
```

## Architecture

Hworld server uses the deskapp framework for all server functionality.
The implementation is intentionally minimal - just configuration and
startup logic. All heavy lifting is done by deskapp.

## Data Persistence

User data is stored in `users.data` in the working directory. When
using Docker, this is persisted in the `/data` volume.
