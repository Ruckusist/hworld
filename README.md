````markdown
# Hworld

A collection of tools and utilities built in the spirit of Unix
philosophy: do one thing well, compose with other tools, and keep
things simple and modular.

## Features

- **Hworld CLI**: Simple Unix-inspired CLI tool
- **Hworld Server**: Network server with authentication and pub/sub
  messaging using the deskapp framework
- **Hworld WebApp**: Browser-based client with terminal-style UI
- **Hworld Client**: Terminal-based TUI client (curses)

## Default Login

All hworld components use a single authentication system:
- **Username**: `dude`
- **Password**: `pass`

(Automatically created on first server startup)

## Project Philosophy

- **Python First**: We prefer Python classes and keep functions small.
- **Clean Code**: 4-space indentation, CamelCase naming, double quotes,
  79-character lines.
- **Self-Contained**: Build our own tools rather than relying on
  external dependencies where possible.
- **Unix Inspired**: Think in terms of pipes, filters, and composable
  components.

## Getting Started

### CLI Tool

1. Clone the repository:
   ```bash
   git clone https://github.com/Ruckusist/hworld.git
   cd hworld
   ```

2. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

4. Run the tool:
   ```bash
   hworld
   ```

### Server

#### Quick Start with Docker

```bash
# Build and run (server + webapp)
./scripts/docker-build.sh
./scripts/docker-run.sh

# Server running on port 28080
# WebApp running on port 8080
# Visit http://localhost:8080 in browser
```

#### Local Development

```bash
# Install dependencies
pip install -e vendor/deskapp
pip install -e .

# Terminal 1: Run server
hworld-server

# Terminal 2: Run webapp
hworld-webapp

# Visit http://localhost:8080
```

#### Terminal Client

```bash
# Connect to local server
hworld-client

# Connect to Docker server
HWORLD_SERVER_HOST=localhost hworld-client
```

See [hworld/server/README.md](hworld/server/README.md),
[hworld/webapp/README.md](hworld/webapp/README.md), and
[hworld/client/README.md](hworld/client/README.md) for detailed
documentation.

## Development

- Follow the coding standards outlined in
  `.github/copilot-instructions.md`
- Keep functions and files small
- Work in complete sections
- Always credit changes in the changelog

## Contributing

1. Create a proposal in `.github/proposals/`
2. Implement changes following project conventions
3. Update the changelog
4. Submit a pull request

## License

[Add license information here]

````
