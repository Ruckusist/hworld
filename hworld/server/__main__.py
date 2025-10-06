# hworld/server/__main__.py
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

"""Hworld Server Entry Point"""

import sys
import time
from hworld.server import Server
from hworld.server.config import ServerConfig


def Main():
    """Start the hworld server"""
    config = ServerConfig()
    server = Server(**config.GetServerArgs())

    print(f"Hworld Server starting on {config.Host}:{config.Port}")

    server.Start()

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.Stop()
        server.EndSafely()
        print("Server stopped.")

    return 0


if __name__ == "__main__":
    sys.exit(Main())
