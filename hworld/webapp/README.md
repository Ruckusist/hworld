# Hworld WebApp
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

## Overview

Hworld webapp is a web-based client for the hworld server. It
provides a browser interface for logging in and interacting with the
server using the deskapp framework.

## Features

- Web-based login interface
- Real-time server communication
- Terminal-style UI (green on black)
- Test/ping functionality
- Built with deskapp.webapp framework

## Quick Start

### Local Development

```bash
# Terminal 1: Start server
hworld-server

# Terminal 2: Start webapp
hworld-webapp

# Visit http://localhost:8080
```

### Docker (Server + WebApp together)

```bash
./scripts/docker-build.sh
./scripts/docker-run.sh

# Server: http://localhost:28080
# WebApp: http://localhost:8080
```

## Usage

1. Open http://localhost:8080 in your browser
2. Enter any username and password (auto-creates account)
3. Click "Login"
4. Click "Test Server (Ping)" to verify connection
5. Click "Logout" when done

## Architecture

```
Browser → WebApp (Flask) → Server (deskapp.server)
         (port 8080)       (port 28080)
```

The webapp acts as a bridge between the browser and the server,
handling HTTP requests and translating them to deskapp Messages.

## API Endpoints

- `GET /` - Main web interface
- `POST /api/login` - Login via server
- `POST /api/test` - Test server connection
- `GET /health` - Health check

## Configuration

Environment variables:
- `HWORLD_SERVER_HOST`: Server hostname (default: localhost)
- `HWORLD_SERVER_PORT`: Server port (default: 28080)

## Files

- `app.py`: Flask application logic
- `templates/index.html`: Main web interface
- `static/style.css`: Terminal-style CSS
- `static/app.js`: Client-side JavaScript
