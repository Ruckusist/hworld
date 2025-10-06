# Hworld Terminal Client
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

## Overview

Hworld terminal client is a curses-based TUI (Text User Interface)
client that connects to the hworld server. It provides an interactive
terminal interface using the deskapp Module framework.

## Features

- Terminal-based UI (curses)
- Connect to local or remote hworld server
- Interactive login
- Test server connection (ping/pong)
- Message history display
- Built with deskapp Module framework

## Quick Start

```bash
# Start the client
hworld-client

# Or with custom server
HWORLD_SERVER_HOST=remote.server.com hworld-client
```

## Usage

### Commands

- `c` - Connect to server
- `l` - Login (prompts for username/password)
- `t` - Test server connection (ping)
- `o` - Logout
- `d` - Disconnect from server
- `q` - Quit

### Workflow

1. Press `c` to connect to server
2. Press `l` to login (enter username and password)
3. Press `t` to test the connection
4. Press `o` to logout
5. Press `q` to quit

## Configuration

Environment variables:
- `HWORLD_SERVER_HOST`: Server hostname (default: localhost)
- `HWORLD_SERVER_PORT`: Server port (default: 28080)

## Connecting to Docker Server

```bash
# Docker server running locally
hworld-client

# Docker server on remote host
HWORLD_SERVER_HOST=192.168.1.100 hworld-client
```

## Architecture

The client is implemented as a deskapp Module, which means:
- Uses deskapp's curses framework
- Inherits Module base class
- Implements Page() for rendering
- Uses deskapp.server.ClientSession for server communication

```
Hworld Client (deskapp Module)
    ↓ ClientSession (TCP Socket)
Hworld Server (deskapp.server)
```

## Development

The client code is organized as:
- `app.py`: HworldClient module class
- `__main__.py`: Entry point with curses setup
- `__init__.py`: Clean exports

Total: ~150 lines of code

## Example Session

```
=== HWORLD CLIENT ===

Status: Connected
Logged in as: alice
Server: localhost:28080

Press 't' to test ping
Press 'o' to logout

=== Messages ===
Connected to localhost:28080
Login successful: alice
Ping successful! Pong received.

Press 'q' to quit
```

## Troubleshooting

**Can't connect to server**
- Verify server is running: `pgrep -f hworld.server`
- Check host and port environment variables
- Test with: `telnet localhost 28080`

**Curses display issues**
- Terminal must support curses
- Try resizing terminal window
- Check TERM environment variable

**Login fails**
- Verify server is accepting connections
- Check server logs
- Try with different username/password
